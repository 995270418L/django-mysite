# django-mysite
由于项目需要必须使用到python，先前已经有了基础，所以花点时间学习一下python的django模板来开发web项目,建个
repository for review it.

## 常用命令

	1. django-admin startprject mysite    -> 新建一个django项目mysite
	2. python manage.py runserver  [host][:][port]       -> 开启服务器(支持热部署除了文件的复制)
	3. python manage.py startapp polls            -> 新建一个应用 polls
	4. python manage.py migrate             -> 创建模板之后需要创建数据库表时执行的语句
	5. python manage.py makemigrations polls   -> 将新添加的应用添加到django中
	6. python manage.py sqlmigrate pools 0001   -> 查看pools应用下0001进程下的建表语句
	7. python manage.py shell          -> 基于Ipython下的有色python shell没啥特点
	8. python manage.py createsuperuser    -> 创建管理员用户
