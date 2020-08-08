# Fibonacci series using recursion

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

n=int(input("Enter the number of terms:"))
if n <= 0:
    print("please enter a +ve number")
else:
    for i in range(n):
        print(fibonacci(i))
