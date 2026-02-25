n=input()
events=list(map(int,input().split()))

officers=0
untreated=0

for i in events:
    if i==-1:
        if officers>0:
            officers-=1
        else:
            untreated+=1
    else:
        officers+=i
print(untreated)
