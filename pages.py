# pages.py 给出了一下调试是常用的页面，不建议对此文件进行修改

import json
import config
import importlib

def image(client):              # 根据用户请求的数据反馈一个图片
    importlib.reload(config)    # 从新加载 configr
    file_type = client.path.split('.')[-1].lower()                    # 最后一个 . 后面的部分是类型名
    if file_type not in config.img_types:                             # 检测文件类型
        raise(Exception('file_type not in config.img_types'))
    try:
        file_name = "." + client.path
        with open(file_name, "rb") as fpin: # 读取整张图片
            image_bytes = fpin.read()
        return config.get_content_type[file_type], image_bytes
    except:
        print(file_name, "not found")
        return page_404(client)
        

def page_404(client): # 返回一个未找到页面
    return 'text/html', "<h1>404 Not Found</h1>".encode('utf-8')

def client_message(client): # 以 json 形式返回所有 clinet 的信息，结合 firefox 使用体验更好
    msg = {}
    for x in client.__dict__: # 枚举 client 的所有信息
        msg[x] = str(client.__dict__[x])
    return 'application/json', json.dumps(msg).encode('utf-8')
