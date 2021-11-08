# 你可以根据你的需要修改 config.py 中的值
import pages

debug = True                # False to disable debug output in the browser
hostName = "localhost"
serverPort = 8080
img_types = ['png', 'jpg', 'ico']

get_content_type = { # 图片文件类型对应的 content-type
    'png': 'image/png',
    'jpg': 'image/jpeg',
    'ico': 'image/x-icon'
}

# 对一些特定前缀指出计算函数，这些计算函数接收一个 client 对象，返回一个 (str, bytes)
# str: Content-Type, bytes: message
prefix = {
    "/favicon.ico$" : (lambda client: pages.image("./favicon.ico")),    # '$' 表示检测字符串结尾
    "/image/"       : (lambda client: pages.image("." + client.path)),  # 得到一张图片
    "/html/"        : (lambda client: pages.html("." + client.path))    # 得到一个静态网页
}