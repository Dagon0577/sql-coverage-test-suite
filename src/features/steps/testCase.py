from behave import *
from suiteCore import *


@When('midware and mysql test case')
def step_impl(context):
    for row in context.table:
        assert compareSQLResult(row['path']) == 1
