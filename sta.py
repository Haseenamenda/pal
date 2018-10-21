def midchenge():
	k=input()
	n=len(k)
	l=list(k)
	k=''
	if n%2!=0:
		for i in range(n//2):
			k+=l[i]
		k+='*'
		j=n//2+1
	else:
		for i in range(n//2-1):
			k+=l[i]
		k+='**'
		j=n//2+1
	for i in range(j,n):
		k+=l[i]
	print(k)
try:
	midchenge()
except:
	print('invalid')
