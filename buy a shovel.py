k, r = map(int, input().split())
shovel=1

while True:
    total=shovel*k
    if total%10==0 or total%10==r:
        print(shovel)
        break
    shovel+=1
