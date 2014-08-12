import webapp2
import os


class MainPage(webapp2.RequestHandler):

  def get(self):
    self.response.headers['Content-Type'] = 'text/html'

    for path in os.listdir(os.path.dirname(__file__)):
      if os.path.isdir(path):
        self.response.out.write('<a href="/%s/">%s</a><br>' %
                                (path, path))


class TransitionPage(webapp2.RequestHandler):

  ROOT = 'index.html'
  ENTERING_TRANSITION = 'transition.css'

  def get(self):
    directory = self.request.path

    self.response.headers['Content-Type'] = 'text/html'
    self.response.headers['Link'] = (
        '<%s%s>;rel=transition-entering-stylesheet;scope=*' %
        (directory, self.ENTERING_TRANSITION))

    with open(os.path.dirname(__file__) + directory + self.ROOT) as f:
      self.response.out.write(f.read())


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/.*/', TransitionPage),
], debug=True)
