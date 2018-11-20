from app.fib import fibs

"""
---------------------------
STEPS:
---------------------------
"""
@given(u'we have the number {number}')
def step_impl(context, number):
    context.fib_number = int(number)

@when(u'we calc the fib')
def step_impl(context):
    context.fib_number = list(fibs(context.fib_number))[-1]

@then(u'we get the fib number {fib_number}')
def step_impl(context, fib_number):
    context.expected_number = int(fib_number)
    assert context.fib_number == context.expected_number, "Calc fib number: %d" % context.fib_number
