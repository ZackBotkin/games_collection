
import tornado.httpserver
import tornado.web
import tornado.ioloop

from settings import STATIC_PATH, TEMPLATE_PATH


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler)
        ]
        settings = {
            "template_path" : TEMPLATE_PATH,
            "static_path" : STATIC_PATH,
        }
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


def main():

    port = 8888

    application = Application()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port)

    print "listening on port %d" % port
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":

    main()
