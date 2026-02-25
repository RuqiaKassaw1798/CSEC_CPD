s=input()
t=input()

current_position=0

for instruction in t:
    if instruction==s[current_position]:
        current_position+=1

print(current_position+1)
