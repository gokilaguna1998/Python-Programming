def main():
	m=int(input())
	l=list(map(int,input().split()))
	for i in range(m):
		prev=l[i]
		co=1
		for j in range(i+1,m):
			if prev >0 and l[j]<0:
				co+=1
			elif prev<0 and l[j]>0:
				co+=1
			prev=l[j]
		print(co,end=" ")
main()
