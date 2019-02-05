def coin(m,1,t):
def coin(m,l,t):
	w=1
	a=0
	s=0
	l.sort(reverse=True)
	for i in range(m):
		while(s<t):
			s=s+l[i]
			a=a+1
	print(a)

def main():
	m=int(input())
	t=int(input())
	l=[]
	for i in range(m):
		l.append(int(input()))
	coin(m,l,t)

try:
	main()
except:
print('invalid')
