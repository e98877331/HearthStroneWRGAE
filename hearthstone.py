import webapp2




class HSArenaLogger(webapp2.RequestHandler):

    def get(self):
        self.response.write('Hello, HS')


application = webapp2.WSGIApplication([
    ('/logArena', HSArenaLogger),
], debug=True)
