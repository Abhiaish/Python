# find second largest element in an array

l=list(map(int,input().split()))
l.sort()
for i in range(0,len(l)):
    l.pop()
    print(l[-1])
    break
    