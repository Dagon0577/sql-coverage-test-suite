# sql-coverage-test-suite

- [Chinese documentation](README-ZH.md)

Compare the result set returned by executing a SQL statement between a distributed database and a traditional relational database.(Temporarily replace the middleware with MySQL, that is, compare MySQL with MySQL)

## Environment configuration

Python3、Docker、behave

## behave

[Official document](https://behave.readthedocs.io/en/latest/tutorial.html)

## Demo
Execute in the ./ directory

>`# sh start.sh`

## Use tutorial (only select is supported for the time being, take test_case as an example)

Create sql folder (such as test) under src / sqls.
Write the corresponding sql file (One SQL statement in the file corresponds to one line. Line breaks are not supported. Each statement ends with a ';'. All lines are commented.)

Create a folder in the src / features directory (such as test)

Write a behave.ini (see the official documentation for the specific parameters, and generally only modify the path of the log)

    ...  
    [handler_File]  
    class=FileHandler  
    args=("../../logs/test.log", 'a')  
    ...

Write a .feature file and pass in the sql folder path (such as testCase.feature)

    Feature: begin a test case
    # Enter feature description here

    Scenario: test case
                When midware and mysql test case
                | path |
                |../../sqls/test/select|

Write a .py file (such as testCase.py)

    from behave import *
    from suiteCore import *


    @When('midware and mysql test case')
    def step_impl(context):
        for row in context.table:
            assert compareSQLResult(row['path']) == 1

sort:

    The end of the sql statement ';' followed by 1 means that the client is not required to perform ascending sorting, and sorting is required by default.

It should be noted that the sql_path here is a relative path, and the current path is the path where the behave is executed. In this case, the current path is src / features / test, not the path src / features / steps where the py file is located.