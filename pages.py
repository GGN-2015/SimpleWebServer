# pages.py 给出了一下调试是常用的页面，不建议对此文件进行修改

import json
import config
import importlib
import method

def image(file_name):            # 根据 filename 反馈一个图片
    importlib.reload(config)     # 从新加载 config
    file_type = method.get_file_type(file_name)                    # 最后一个 . 后面的部分是类型名
    if file_type not in config.img_types:                          # 检测文件类型
        # raise(Exception('file_type[%s] not in config.img_types' % file_type))
        return page_404()
    try:
        with open(file_name, "rb") as fpin: # 读取整张图片
            image_bytes = fpin.read()
        return config.get_content_type[file_type], image_bytes
    except:
        print("image: " + file_name + " not found")
        return page_404()

def html(file_name): # 直接根据用户请求给出一个 html 文件
    file_type = method.get_file_type(file_name)
    if file_type != "html":
        # raise(Exception('file_type[%s] is not html' % file_type))
        return page_404()
    try:
        with open(file_name, "r", encoding='utf-8') as fpin: # 读取整个 html
            image_bytes = fpin.read()
        return "text/html", image_bytes.encode('utf-8')
    except:
        print("html: " + file_name + "not found")
        return page_404()

def page_404(): # 返回一个未找到页面
    return 'text/html', "<h1>404 Not Found</h1>".encode('utf-8')

def client_message(client): # 以 json 形式返回所有 clinet 的信息，结合 firefox 使用体验更好
    msg = {}
    for x in client.__dict__: # 枚举 client 的所有信息
        msg[x] = str(client.__dict__[x])
    return 'application/json', json.dumps(msg).encode('utf-8')
