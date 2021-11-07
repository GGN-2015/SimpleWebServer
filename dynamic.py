# 你需要实现 get_return_message 从而实现服务器的各种功能

import pages # 定义了一些常用的页面信息

def get_return_message(client):
    # client.path 可以看到 Get 方法的路径
    # client.address 可以看到用户的 IP 和端口
    return pages.client_message(client)