
# 安装

sql2excel可以基于python环境运行，同时也可以打包成windows上的可执行文件。打包使用的是pyinstaller，可以通过pip进行安装。以下教程主要是针对于没有安装python环境，且电脑权限受限，难以进行环境变量配置的用户。

## 安装python

推荐安装python3.7，可以从官网下载完整安装包。完整安装包包含pip在内的工具，可以避免安装pip的麻烦。

## 配置临时环境变量

如果已经安装了pip等工具，打开cmd命令窗口，输入以下指令以配置Python和pip的临时环境变量：

```shell
set PATH=<Python安装地址>;<Python安装地址>\Scripts;%PATH%
```

如果没有安装pip，则先输入以下指令以配置Python的临时环境变量：

```shell
set PATH=<Python安装地址>;%PATH%
```

然后，输入以下指令来安装pip：

```shell
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

安装成功后，将pip的路径加入到临时环境变量中：

```shell
set PATH=<Python安装地址>\Scripts;%PATH%
```

## 安装pyinstaller

输入以下指令：

```shell
pip install pyinstaller
```

## 将sql2excel.py打包成windoes可执行文件

输入以下指令：

```shell
py2installer -F sql2excel.py --noconsole
```

这里--noconsole的作用是，防止程序运行时会有console窗口打开。
