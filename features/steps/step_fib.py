from app.fib import fibs

"""
---------------------------
STEPS:
---------------------------
"""
@given(u'we have the number 10')
def step_impl(context):
    context.fib_number = 10

@when(u'we calc the fib')
def step_impl(context):
    context.fib_number = list(fibs(context.fib_number))[-1]

@then(u'we get the fib number 55')
def step_impl(context):
    context.expected_number = 55
    assert context.fib_number == context.expected_number, "Calc fib number: %d" % context.fib_number
