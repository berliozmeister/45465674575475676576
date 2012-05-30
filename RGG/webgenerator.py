import web
import os
import urllib
import posixpath

from igraph import *


urls = (
    '/(.*)', 'index'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

def dummy(n):
    G = Graph.Barabasi(n, 1, zero_appeal=1)
    layout = G.layout_circle()
    svgname = "generated/graph-%s-.svg" % str(n)          
    G.write_svg(svgname, layout)


class index:
    def GET(self, wtf):
        inp = web.input(mean='10', power='2', size='30')
        dummy(int(inp.size))
        return render.index(mean=inp.mean, power=inp.power, size=inp.size)

class StaticMiddleware:
    """WSGI middleware for serving static files."""
    def __init__(self, app, prefix='/generated/',
                 root_path=r'/generated/'):
        self.app = app
        self.prefix = prefix
        self.root_path = root_path

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '')
        path = self.normpath(path)

        if path.startswith(self.prefix):
            environ["PATH_INFO"] = os.path.join(self.root_path,
                                                web.lstrips(path, self.prefix))
            return web.httpserver.StaticApp(environ, start_response)
        else:
            return self.app(environ, start_response)

    def normpath(self, path):
        path2 = posixpath.normpath(urllib.unquote(path))
        if path.endswith("/"):
            path2 += "/"
        return path2


if __name__ == "__main__":
    wsgifunc = app.wsgifunc()
    wsgifunc = StaticMiddleware(wsgifunc)
    wsgifunc = web.httpserver.LogMiddleware(wsgifunc)
    server = web.httpserver.WSGIServer(("0.0.0.0", 8080), wsgifunc)
    print "http://%s:%d/" % ("0.0.0.0", 8080)
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
