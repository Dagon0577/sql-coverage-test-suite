# sql-coverage-test-suite
比较在分布式数据库和传统关系数据库之间执行SQL语句所返回的结果集。（暂时用MySQL代替中间件，即MySQL与MySQL比较,MySQL版本为5.7.21）

## 环境配置

Python3、Docker、behave

[参考文档](environment-ZH.md)

## behave

[官方文档](https://behave.readthedocs.io/en/latest/tutorial.html)

## 演示
在./目录下执行

>`# sh start.sh`

## 使用教程（暂时只支持select，以test_case为例）

在src/sqls下建立sql文件夹（如test）。
编写相应的sql文件（文件中一条SQL语句对应一行，不支持换行，每条语句以';'结尾。注释一律换行。）

在src/features目录下建立一个文件夹（如test）

编写一个behave.ini（具体参数看官方文档，一般情况只用修改日志的路径）

    ...  
    [handler_File]  
    class=FileHandler  
    args=("../../logs/test.log", 'a')  
    ...

编写一个.feature文件,传入sql文件夹路径（如testCase.feature)

    Feature: begin a test case
    # Enter feature description here

    Scenario: test case
                When midware and mysql test case
                | path |
                |../../sqls/test/select|

编写一个.py文件（如testCase.py)

    from behave import *
    from suiteCore import *


    @When('midware and mysql test case')
    def step_impl(context):
        for row in context.table:
            assert compareSQLResult(row['path']) == 1

排序：
    
    sql语句结尾';'后面跟1代表不需要客户端执行升序排序，默认需要排序。

需要注意的是，这里的sql_path用的是相对路径，而当前路径为执行behave时所在路径。如此时，当前路径为src/features/test，并不是该py文件所在路径src/features/steps。