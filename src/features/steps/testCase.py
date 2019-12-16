from behave import *
from suiteCore import *


@When('midware and mysql test case data')
def step_impl(context):
    sql_path = "../../sqls/test/select"
    assert compareSQLResult(sql_path) == 1
