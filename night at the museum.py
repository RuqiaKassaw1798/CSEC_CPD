s=input()
current="a"
total_moves=0

for char in s:
    dis=abs(ord(char)-ord(current))
    moves=min(dis, 26-dis)
    total_moves+=moves
    current=char
print(total_moves)
