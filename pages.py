# pages.py 给出了一下调试是常用的页面，不建议对此文件进行修改

import json

def page_404(client): # 返回一个未找到页面
    return 'text/html', "<h1>404 Not Found</h1>".encode('utf-8')

def client_message(client): # 以 json 形式返回所有 clinet 的信息，结合 firefox 使用体验更好
    msg = {}
    for x in client.__dict__: # 枚举 client 的所有信息
        msg[x] = str(client.__dict__[x])
    return 'application/json', json.dumps(msg).encode('utf-8')
