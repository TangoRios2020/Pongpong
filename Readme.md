测试数据使用方法
1 在 ~/.bashrc 中定义使用到的环境变量
2 在 Role 表中添加角色, 在 flask shell 环境中执行 Role.insert_roles() 方法
3 在 flask shell 中导入 fake 并生成对应的 fake data 测试使用.
4 在 Model 中编辑模型后, 需要使用 flask db migrate 和 flask db upgrade 进行数据库升级
6 执行 flask run 运行程序.