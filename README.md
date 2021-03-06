### Smart CS

[![Django](https://img.shields.io/badge/django-2.1-brightgreen.svg?style=plastic)](https://www.djangoproject.com/)[![Python3](https://img.shields.io/badge/python-3.6-green.svg?style=plastic)](https://www.python.org/)[![Ansible](https://img.shields.io/badge/ansible-2.4.2.0-blue.svg?style=plastic)](https://www.ansible.com/)[![Paramiko](https://img.shields.io/badge/paramiko-2.4.1-green.svg?style=plastic)](http://www.paramiko.org/)

- Smart CS是基于jumpserver(`v1.4.6`)二次开发的开源云运维安全审计系统. 旨在运维人员更加便捷的批量管理各类服务器.

#### 特色功能

1. **公有云/主机系统用户导入**

   用户可通过模板进行批量导入公有云所属资产/IDC上的系统用户到堡垒机中,用于系统用户,灵活配置资产的授权策略, 使用户更加方便的管理资产

2. **云资产一键导入及同步**

   - 用户通过各云账号进行批量导入云资产
   - 支持目前支持 `阿里云`,`腾讯云`
   - 根据资产所属项目自动分配节点.

#### 使用说明
- 见说明文档
- 安装coco服务参考:[安装COCO]

#### Jumpserver 项目结构说明

- 个别目录不全 

    ```html
     .
    ├── apps                             // 管理后台目录,也是各apps 所在目录
    │   ├── assets                       // 资产管理app(应用)
    │   │   ├── api                      // Restful api 逻辑代码,views模块对应
    │   │   ├── forms                    // form表单模块
    │   │   ├── migrations               // Models Migrations 版本控制目录 
    │   │   ├── models                   // ORM 数据库模块
    │   │   ├── serializers              // 将请求或数据库对象序列化python可读对象
    │   │   ├── templates                // 模板文件,使用层级模板,防止重名
    │   │   ├── templatetags             // 模板标签目录
    │   │   ├── urls                     // 视图函数与路由映射,包含api url 
    │   │   └── views                    // 视图函数模块
    │   │   ├── apps.py                  // 新版本 Django APP 设置文件,定义app命名
    │   │   ├── const.py                 // 常量配置文件
    │   │   ├── hands.py                 // 与其他app存在交互的模块相互调用               
    │   │   ├── tests.py                 // 测试用例文件
    │   │   ├── utils.py                 // 该app下的通用的函数方法
    │   │   ├── __init__.py              // 对外暴露的接口,放到该文件中,方便别的 APP 引用
    │   ├── audits                       // 日志审计app
    │   ├── authentication               // 用户认证模块(安全组件)
    │   ├── common                       // 系统设置app(email发送,terminal终端操作,设置) 
    │   ├── fixtures                     // 初始化数据目录
    │   │   ├── fake.json                // 生成大量测试数据    
    │   │   └── init.json                // 初始化项目数据库
    │   ├── jumpserver                   // 项目设置app
    │   │   ├── conf.py                  // 加载配置文件 
    │   │   ├── context_processor.py 
    │   │   ├── __init__.py
    │   │   ├── middleware.py            // 中间件文件
    │   │   ├── settings.py              // 项目设置文件
    │   │   ├── swagger.py
    │   │   ├── urls.py                  // 项目入口 Url(顶层url)
    │   │   ├── utils.py              
    │   │   ├── views.py                 // 视图函数
    │   │   └── wsgi.py                  // django框架WSGI服务器
    │   ├── locale                       // 项目多语言目录
    │   │   └── zh    
    │   ├── __init__.py                  // apps对外暴露接口
    │   ├── manage.py                    // 管理项目脚本文件
    │   ├── ops                          // 作业中心app(命令行)
    │   ├── orgs
    │   ├── perms                        // 权限管理 app
    │   ├── static                       // 顶层 静态文件
    │   ├── templates                    // 顶层templates
    │   ├── terminal                     // 是按web terminal app 
    │   └── users                        // 用户管理 app
    ├── build.sh                         // 自动构建脚本
    ├── config_example.yml               // 配置文件样例
    ├── config.yml                       // 生产环境配置文件
    ├── data                             
    │   ├── celery
    │   ├── media
    │   └── static
    ├── Dockerfile                       // docker 安装文件
    ├── docs                             // 所有 DOC 文件放到该目录
    ├── entrypoint.sh
    ├── jms							     // 启动脚本
    ├── LICENSE
    ├── logs                             // 日志目录
    ├── README.md                        // README 文档
    ├── requirements                     // 各系统依赖包
    │   ├── mac_requirements.txt
    │   ├── requirements.txt
    │   └── rpm_requirements.txt
    ├── run_server.py                     // 启动文件
    ├── tmp                               // 进程文件
    │   ├── beat.pid
    │   ├── celery.pid
    │   └── gunicorn.pid
    └── utils                             // 通用函数
    ```
```

```
