from myhandler import MainPage
from webapp2 import WSGIApplication
app = WSGIApplication([('.*', MainPage)], debug=True)
