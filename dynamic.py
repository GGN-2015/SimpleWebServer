# 你需要实现 get_return_message 从而实现服务器的各种功能

import pages # 定义了一些常用的页面信息
import method # 定义了一些常用计算性算法
import config
import importlib

def get_return_message(client):  # 核心计算函数
    path = client.path
    importlib.reload(pages)      # 只在测试的时候 reload pages 和 method
    importlib.reload(method)
    importlib.reload(config)
    for prefix in config.prefix: # 对配置文件中钦定的一些前缀，采用指定的函数计算得到页面
        if method.has_prefix(path, prefix):
            func = config.prefix[prefix]
            return func(client)
    raise(Exception('Unhandled url type: url=%s' % path))
