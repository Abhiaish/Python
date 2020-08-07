# find first and last digit of a number.

n=input()
a=[]
for i in range(0,len(n)):
    a.append(n[0])
    a.append(n[-1])
    print(a)