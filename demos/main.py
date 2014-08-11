import webapp2
import os

class StarryNightResultsPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.headers['Link'] = '<transition.css>;rel=transition-entering-stylesheet;scope=*'

        path = os.path.join(os.path.split(__file__)[0], 'starry_night_results/index.html')
        with open(path) as f:
            self.response.out.write(f.read())

application = webapp2.WSGIApplication([
    ('/starry_night_results/.*', StarryNightResultsPage),
], debug=True)

