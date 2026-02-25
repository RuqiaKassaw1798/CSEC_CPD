n=int(input())
home=[]
guest=[]

for i in range(n):
    h, g=list(map(int, input().split()))
    home.append(h)
    guest.append(g)
count=0

for h_color in home:
    for g_color in guest:
        if h_color==g_color:
            count+=1
print(count)
