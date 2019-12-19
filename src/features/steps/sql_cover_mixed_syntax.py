from behave import *
from suiteCore import *


@When('midware and mysql sql_cover_mixed_syntax test')
def step_impl(context):
    for row in context.table:
        assert executeSQL(row['path']) == 1
