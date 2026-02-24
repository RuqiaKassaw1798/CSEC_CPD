n, h = map(int, input().split())
print(sum(2 if int(x) > h else 1 for x in input().split())) 
