# 环境配置：Python3、Docker、behave

参考文档，具体情况视自身而定。
## Python3安装
1、找到系统现在的python的位置

    $ whereis python

    python: /usr/bin/python2.7 /usr/bin/python /usr/lib/python2.7 /usr/lib64/python2.7 /etc/python /usr/include/python2.7 /usr/share/man/man1/python.1.gz

可以知道python在 /usr/bin目录中

    $ cd /usr/bin/
    $ ll python*


    lrwxrwxrwx. 1 root root    7 2月   7 09:30 python -> python2
    lrwxrwxrwx. 1 root root    9 2月   7 09:30 python2 -> python2.7
    -rwxr-xr-x. 1 root root 7136 8月   4 2017 python2.7

可以看到，python指向的是python2，python2指向的是python2.7，因此我们可以装个python3，然后将python指向python3，然后python2指向python2.7，那么两个版本的python就能共存了。

先安装相关包，用于下载编译python3

    $ yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make

运行了以上命令以后，就安装了编译python3所用到的相关依赖

运行这个命令添加epel扩展源

    $ yum -y install epel-release

安装pip3

    $ yum install python3-pip

pip3安装wget

    $ pip3 install wget

wget下载python3的源码包

    $ wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tar.xz

编译python3源码包

解压

    $ xz -d Python-3.6.4.tar.xz
    $ tar -xf Python-3.6.4.tar

进入解压后的目录，依次执行下面命令进行手动编译

    $ ./configure prefix=/usr/local/python3
    $ make && make install

如果最后没提示出错，就代表正确安装了，在/usr/local/目录下就会有python3目录

将原来的链接备份

    $ mv /usr/bin/python /usr/bin/python.bak

添加python3的软链接

    $ ln -s /usr/local/python3/bin/python3.6 /usr/bin/python

测试是否安装成功了

    $ python -V

更改yum配置，因为其要用到python2才能执行，否则会导致yum不能正常使用

    vi /usr/bin/yum
    把#! /usr/bin/python修改为#! /usr/bin/python2

    vi /usr/libexec/urlgrabber-ext-down
    把#! /usr/bin/python 修改为#! /usr/bin/python2


## Docker安装

- 1、先卸载旧版本的docker

>`$ sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine`

旧版本的内容在 /var/lib/docker 下，目录中的镜像(images), 容器(containers), 存储卷(volumes), 和 网络配置（networks）都可以保留。

Docker CE 包，目前的包名为 docker-ce。

- 2、安装Docker

为了方便添加软件源，支持 devicemapper 存储类型，安装如下软件包

>`$ sudo yum update`

>`$ sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2 `


添加 Docker 稳定版本的 yum 软件源
>`$ sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo`

更新一下 yum 软件源的缓存，并安装 Docker。
>`$ sudo yum update`
>`$ sudo yum install docker-ce`

如果弹出 GPG key 的接收提示，请确认是否为 060a 61c5 1b55 8a7f 742b 77aa c52f eb6b 621e 9f35，如果是，可以接受并继续安装。

至此，Docker 已经安装完成了，Docker 服务是没有启动的，操作系统里的 docker 组被创建，但是没有用户在这个组里。

    注意

    默认的 docker 组是没有用户的（也就是说需要使用 sudo 才能使用 docker 命令）。
    您可以将用户添加到 docker 组中（此用户就可以直接使用 docker 命令了）。

加入Docker用户组命令

`$ sudo usermod -aG docker USER_NAME`

用户更新组信息后，重新登录系统即可生效。

如果想安装指定版本的 Docker，可以查看一下版本并安装。

>`$ yum list docker-ce --showduplicates | sort -r`

可以指定版本安装,版本号可以忽略 `:` 和 `el7`，如 docker-ce-18.09.1

>`$ sudo yum install docker-ce-<VERSION STRING>`

至此，指定版本的 Docker 也安装完成，同样，操作系统内 docker 服务没有启动，只创建了 docker 组，而且组里没有用户。

- 3、启动Docker

如果想添加到开机启动

>`$ sudo systemctl enable docker`

启动Docker服务

>`$ sudo systemctl start docker`

验证 Docker CE 安装是否正确，可以运行 hello-world 镜像

>`$ sudo docker run hello-world`

- 4、安装Docker-compose

从github上下载docker-compose二进制文件安装

下载最新版的docker-compose文件 

    $ sudo curl -L https://github.com/docker/compose/releases/download/1.19.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

添加可执行权限

    $ sudo chmod +x /usr/local/bin/docker-compose

测试安装结果

    $ docker-compose --version 


## behave安装

安装behave、pymysql
>`# pip3 install behave`

>`# pip3 install pymysql`

