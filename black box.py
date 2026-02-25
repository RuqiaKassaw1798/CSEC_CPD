a=list(map(int, input().split()))
s=input()

total=0

for char in s:
    index=int(char)-1
    total+=a[index]
print(total)
