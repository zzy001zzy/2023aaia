k = int(input())
total=0
for i in range(1,1001):
	total+=i
	if total>k:
		ans=i
		break
print(ans,end='')