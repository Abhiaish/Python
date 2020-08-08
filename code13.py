# print all negative elements in an array.
l=list(map(int,input().split()))
for i in range (0,len(l)):
    if l[i]<0:
        print(l[i])