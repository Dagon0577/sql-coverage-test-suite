from behave import *
from suiteCore import *


@When('midware and mysql sql_cover_mixed_select test')
def step_impl(context):
    for row in context.table:
        assert compareSQLResult(row['path']) == 1
