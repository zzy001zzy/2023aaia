a = list(map(int,input().split()))
ans=0
for i in a:
	if i%3==0:ans+=1
print(ans)