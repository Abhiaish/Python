#  Print all Prime Numbers in an Interval

n=int(input())
m=int(input())

print("the numbes between",n ,"and",m ,"are:")

for i in range(n,m+1):
    # print(i)
    if(i>1):
        for j in range (2,i):
            # print(j)
            if(i % j == 0):
                break
        else:
            print(i)