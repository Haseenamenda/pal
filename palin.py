s=input()
def pal(n):
	a=n[::-1]
	return a
n=pal(s)
if s.isalpha():
	if(n==s):
		print("YES")
	else:
		print("No")
