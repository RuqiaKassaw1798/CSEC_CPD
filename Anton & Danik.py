n = int(input())
results = input()

anton = 0
danik = 0

for game in results:
    if game == 'A':
        anton += 1
    else:
        danik += 1

if anton > danik:
    print("Anton")
elif danik > anton:
    print("Danik")
else:
    print("Friendship")
