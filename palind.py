s=input()
def pal(m):
	a=m[::-1]
	return a
m=pal(s)
if s.isalpha():
	if(m==s):
		print("yes")
	else:
		print("no")
