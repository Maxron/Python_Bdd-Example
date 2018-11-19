"""
----------------------------
-PROBLEM DOMAIN:
----------------------------
-"""
def fibs(num):
    a = b = 1
    for i in range(num):
        yield a
        a, b = b, a + b
