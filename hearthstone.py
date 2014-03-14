import webapp2
import random
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

class HSArenaLogger(webapp2.RequestHandler):

    def get(self):
        counterq = ArenaGameCounter.query()
        counters = counterq.fetch()
        for idx, counter in enumerate(counters):
           # self.response.write('wtf dd')
            self.response.write('counter ' + str(idx) +' :content<br />')
            self.response.write("win: " + str(counter.winCountList) +' <br />')
            self.response.write("total: " + str(counter.totalCountList) +' <br />')
        self.response.write(MAIN_HTML)

    def post(self):
        counterq = ArenaGameCounter.query()
        counters = counterq.fetch(1)
        if not counters:
            counter = ArenaGameCounter(id=DEFAULT_DATA_SET)
            counter.winCountList = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            counter.totalCountList = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        else:
            counter = counters[0]
        rd = random.randint(0,8)
        #TODO wrong code here
        roleType = int(self.request.get('roleType'))
        isWin  =self.request.get('isWin')
        counter.winCountList[roleType] += 1
        if isWin == 'true':
            counter.totalCountList[roleType] += 1
        counter.put()
        self.redirect('/logArena')

application = webapp2.WSGIApplication([
    ('/logArena', HSArenaLogger),
], debug=True)
