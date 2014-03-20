import webapp2
import json
import logging
from google.appengine.ext import ndb


DEFAULT_DATA_SET = 'first'


def data_key(dataSet=DEFAULT_DATA_SET):
    """Constructs a Datastore key for a Guestbook entity with\
    guestbook_name."""
    return ndb.Key('HSDataSet', dataSet)


class ArenaGameCounter(ndb.Model):
    winCountList = ndb.IntegerProperty(repeated=True)
    totalCountList = ndb.IntegerProperty(repeated=True)


MAIN_HTML = """\
    <form action="/logArena" method="post">
      <div>
        <input type="submit" value="go">
      </div>
    """


def initAll():
    for i in range(0, 9):
        counter = ArenaGameCounter.get_by_id(str(i))
        logging.debug("iiiiiiiiiiiiiiiiiiiiiii %s", str(counter))

        if counter is None:
            counter = ArenaGameCounter(id=str(i))
            counter.winCountList = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            counter.totalCountList = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            counter.put()


class ArenaInitializer(webapp2.RequestHandler):
    def get(self):
        self.response.write('hello world')

    def post(self):
        if self.response.get('ApiKey') == 'towolf':
            initAll()


class HSArenaLogger(webapp2.RequestHandler):

    def get(self):
        counterq = ArenaGameCounter.query()
        counters = counterq.fetch()

        self.response.content_type = 'application/json'
        obj = None
        objs = [];
        #print(repr(counters))
        for idx, counter in enumerate(counters):
            obj = {'roleType': idx,
                   'vsWinCountList': counter.winCountList,
                   'vsTotalCountList': counter.totalCountList}
            objs.append(obj)
        self.response.write(json.dumps(objs))
        #for idx, counter in enumerate(counters):
        #   # self.response.write('wtf dd')
        #   self.response.write('counter ' + str(idx) +' :content<br />')
        #   self.response.write("win: " + str(counter.winCountList) +' <br />')
        #   self.response.write("total: " + str(counter.totalCountList) +' <br />')
        #self.response.write(MAIN_HTML)

    def post(self):
        counterq = ArenaGameCounter.query()
        counters = counterq.fetch()
        if len(counters) < 9:
            initAll()

        roleType = self.request.get('roleType')
        counter = ArenaGameCounter.get_by_id(roleType)
        #if counter is None:
        #    counter = ArenaGameCounter(id=roleType)
        #    counter.winCountList = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        #    counter.totalCountList = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        vsRoleType = int(self.request.get('vsRoleType'))
        isWin = self.request.get('isWin')

        counter.totalCountList[vsRoleType] += 1
        if isWin == 'true':
            counter.winCountList[vsRoleType] += 1
        counter.put()
        self.redirect('/logArena')

application = webapp2.WSGIApplication([
    ('/logArena', HSArenaLogger),
    ('/logArena/init', ArenaInitializer),
], debug=True)
