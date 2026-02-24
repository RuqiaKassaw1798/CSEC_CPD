n=input()
boxes=list(map(int,input().split()))

boxes.sort()

print(*sorted(boxes))
