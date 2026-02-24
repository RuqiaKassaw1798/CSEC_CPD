n = int(input())
count_solved = 0

for i in range(n):
    opinions = list(map(int, input().split()))
    
    if sum(opinions) >= 2:
        count_solved += 1

print(count_solved)
