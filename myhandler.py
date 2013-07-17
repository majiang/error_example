from google.appengine.ext.webapp import RequestHandler

class MyHandler(RequestHandler):
    def write_out(self, file_name, content):
        from google.appengine.ext.webapp.template import render
        from os.path import join, dirname
        self.response.out.write(render(
          join(join(dirname(__file__), 'template'), file_name + '.html'),
          content
        ))

class MainPage(MyHandler):
    def get(self):
        self.write_out('main/main', {})
