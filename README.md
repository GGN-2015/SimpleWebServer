# SimpleWebServer

2021-07-11 开发初期，什么都没有。—— $\text{GGN\_2015}$

## 启动服务器

```shell
nohup sudo python3 server.py &
disown %1
```

## 配置与修改

修改 ``dynamic.py`` 中的 ``get_return_message`` 函数，从而定义自己想要返回的页面/信息。

修改 ``config.py`` 中的变量的值从而更改服务器的配置。

以上两个文件在运行时会被 ``server.py`` 动态加载，因此，可以在服务器运行时修改这两个文件。

