N=int(input())
L,R=map(int,input().split())
for i in range(L,R):
	if(i==N):
		print("yes")
		break
else:
	print("no")
