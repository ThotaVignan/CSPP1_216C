def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def div(a,b):
    assert (b == 0),"b value can be ZERO"
    # print(a/b)
def mul(a,b):
    print(a*b)
a,b = 5,0
# try:
add(a,b)
sub(a,b)
div(a,b)
# except Exception as e:
#     print(e)
# finally:
mul(a,b)
