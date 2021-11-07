# 您不需要对 server.py 进行修改，除非您觉得程序中的实现有问题

from  http.server import HTTPServer,BaseHTTPRequestHandler
import dynamic      # 用户自己编写的代码
import importlib    # 用于 reload
import traceback    # 用于输出错误信息
import html         # html.escape / html.unescape
import config       # config 中有一些配置信息

def get_return_message(client):
    try:
        importlib.reload(dynamic) # 重新加载 python 库
        content_type, bytes_message = dynamic.get_return_message(client)
        return content_type, bytes_message
    except:
        importlib.reload(config) # 使用 config 中的值动态决定是否需要输出错误信息
        bytes_message = "<p>Error</p>"
        if config.debug:
            bytes_message += "<p>"
            bytes_message += html.escape(traceback.format_exc().replace('\t', " " * 4)).replace('\n', "<br>")
            bytes_message += "</p>"
            bytes_message += "<p>use 'config.debug = False' to disable the error message!</p>"
            # 使用 html.escape 来生成转义字符
            # 使用 html.unescape 来消除转义字符
        return 'text/html', bytes_message.encode('utf-8') # 返回错误信息

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):                                               # the do_GET method is inherited from BaseHTTPRequestHandler
        self.send_response(200)                                     # 这里简单粗暴的直接返回了 200 OK
        content_type, bytes_message = get_return_message(self)      # 调用 dynamic 中实现的 get_return_message 函数计算返回结果
        self.send_header("Content-type", content_type)              # content_type = 'text/html'
        self.send_header("Content-length", len(bytes_message))
        self.end_headers()
        self.wfile.write(bytes_message)                             # 反馈一个 HTML 页面/图片二进制信息/json

if __name__ == "__main__":
    webServer = HTTPServer((config.hostName, config.serverPort), MyServer)
    print("Server started http://%s:%s" % (config.hostName, config.serverPort))  #Server starts
    try:
        webServer.serve_forever()
    except KeyboardInterrupt: # 支持键盘中断
        pass
    webServer.server_close()  #Executes when you hit a keyboard interrupt, closing the server
    print("Server stopped.")