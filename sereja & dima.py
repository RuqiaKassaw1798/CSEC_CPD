n=int(input())
cards=list(map(int,input().split()))

sereja=0
dima=0

left, right=0, n-1
sereja_turn=True

while left<=right:
    if cards[left]>cards[right]:
        picked_card=cards[left]
        left+=1
    else:
        picked_card=cards[right]
        right-=1
    if sereja_turn:
        sereja+=picked_card
    else:
        dima+=picked_card
    
    sereja_turn=not sereja_turn
print(sereja,dima)
        
