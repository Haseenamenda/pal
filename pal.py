b=input()
def pal(x):
	a=x[::-1]
	return a
x=pal(b)
if b.isalpha():
	if(x==b):
		print("YES")
	else:
		print("No")
