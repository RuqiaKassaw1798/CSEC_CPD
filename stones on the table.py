n=int(input())
stones=input()
removals=0

for i in range(n-1):
    if stones[i]==stones[i+1]:
        removals+=1
print(removals)
