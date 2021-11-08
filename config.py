# 你可以根据你的需要修改 config.py 中的值

debug = True                # False to disable debug output in the browser
hostName = "localhost"
serverPort = 8080
img_types = ['png', 'jpg', 'ico']

get_content_type = { # 图片文件类型对应的 content-type
    'png': 'image/png',
    'jpg': 'image/jpeg',
    'ico': 'image/x-icon'
}