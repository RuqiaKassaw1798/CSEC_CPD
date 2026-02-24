s=input()
lower_count=0
upper_count=0

for char in s:
    if char.islower():
        lower_count+=1
    else: 
      upper_count+=1
    
if lower_count>=upper_count:
    print(s.lower())
else:
   print(s.upper())
