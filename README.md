## Flask部署
### 1. 环境
* OS：CentOS7 x86_64
* Python: 3.6
* Django: 2.2
* uwsgi: 2.0
* Nginx或Openresty
* Sqlite: 3.28.0
### 2. 卸载预装sqlite-3.7
```bash
rpm -e --nodeps sqlite-3.7.17-8.el7.x86_64
rpm -qa |grep nginx
```
### 3. 安装Python36
```bash
yum install python36-devel
```
### 4. 创建并激活虚拟环境
```bash
python3 -m venv venv
. venv/bin/activate
```
### 5. Django2.2升级安装sqlite3.28.0
> https://wangbin.io/blog/it/django2.2-sqlite3.html

#### 依赖安装
```bash
yum install gcc
yum install autoconf automake libtool
```

#### 安装步骤
* 下载tar.gz
* ./configure --prefix=/usr/local/sqlite
* autoreconf –vfi
* make
* make install
* ln -fs /usr/local/sqlite/bin/sqlite3 /usr/bin/sqlite3
* 动态库  LD_LIBRARY_PATH=/usr/local/sqlite/lib:$LD_LIBRARY_PATH
* export LD_LIBRARY_PATH
* ldconfig
### 5. 安装uwsgi
```bash
pip install uwsgi
```
### 6. 安装nginx或openresty
```bash
yum install nginx
yum install openresty
```

### 8. 在项目目录下添加uwsgi.ini配置
```ini
[uwsgi]
# 通过uwsgi访问django需要配置成http
# 通过nginx请求uwsgi来访问django 需要配置成socket
# 9000 是django的端口号
socket = :9000

# web项目根目录
chdir = /mnt/data/liupan/gcs-django

# module指定项目自带的的wsgi配置文件位置，项目名称
module = learning_log.wsgi

# 虚拟环境的python_home目录
home = /mnt/data/liupan/gcs-django/venv

# 允许存在主进程
master = true

# 开启进程数量
processes = 3

# 服务器退出时自动清理环境
vacuum = true
```
### 7. 测试运行项目
```bash
# 安装依赖
pip install -r requirements.txt
# 创建数据库
python manage.py migrate
# 测试运行
python manage.py runserver

# uwsgi启动
uwsgi --ini django_uwsgi.ini
```

### 9. uwsgi启动、停止、重启
```bash
uwsgi --ini django_uwsgi.ini
uwsgi --stop django_uwsgi.pid
uwsgi --reload django_uwsgi.pid
```

### 10. nginx配置
```nginx
location / {
       include /usr/local/openresty/nginx/conf/uwsgi_params;
       uwsgi_pass 127.0.0.1:9000;
   }
   location /index/ {
       root /index/;
   }
   location /static{
       alias /mnt/data/liupan/gcs-django;
   }
```