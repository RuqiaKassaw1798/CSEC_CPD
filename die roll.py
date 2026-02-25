
y, w=map(int, input().split())
 
m=max(y,w)
win=6-m+1
 
match win:
    case 1:
        print("1/6")
    case 2:
        print("1/3")
    case 3:
        print("1/2")
    case 4:
        print("2/3")
    case 5:
        print("5/6")
    case 6:
        print("1/1")
