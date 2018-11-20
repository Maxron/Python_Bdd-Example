Feature: Calc fib

   In order to introduce Behave
   We calc fib as example

   Scenario Outline: Scenario Outline name: Calc fib number
   Given we have the number <number>
   When we calc the fib
   Then we get the fib number <fib_number>

    Examples: Some numbers
    | number | fib_number |
    |   1    |      1     |
    |   2    |      2     |
    |   10   |      55    |
