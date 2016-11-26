#coding:utf-8
import tornado.web 
import tornado.ioloop
import tornado.httpserver
import tornado.options


from tornado.options import define,options
from tornado.web import RequestHandler,url

tornado.options.define('port',type=int,default=8000,help='服务器端口')
# tornado.options.define('oprt',type=int,default=8000,help='服务器端口')

class IndexHandler(tornado.web.RequestHandler): 
	# 处理类
	def get(self):
		self.write('<a href = "+ self.reverse_url("cpp_py") +">cpp</a>')

class Sub(RequestHandler):
	def initialize(self,subject):
		self.subject = subject

	def get(self):
		self.write(self.subject)


if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application(
	      [(r"/",IndexHandler),
	      url(r"/python",Sub,{"subject":"c++"},name = "cpp_py"),
	      url(r"/cpp",Sub,{"subject":"python"},name = "cpp_url"),
	      ],
	      debug = True
	      )


	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.current().start()