a = input()
N = len(a)
for i in range(N):
	if i!=0 and (N-i)%3==0:
		print(',',end='')
	print(a[i],end='')