def add(a,b):
	print("Ädd",a+b)
def sub(a,b):
	print("sub",a-b)
def div(a,b):
	assert(b>0),"div err----"
	print("div",a/b)
def mul(a,b):
	print("mul",a*b)
a,b = 5,0

try:
	add(a,b)
	sub(a,b)
	if b <=0:
		raise Exception("can't perform")
	div(a,b)
except Exception as e:
	print(e,"     Ecxeption error")
# 	print("div error")
# else:
# 	mul(a,b)
finally:
	mul(a,b)
