def factorial(n):
    result = 1
    for x in range(1,n):
        result *= x 
    return result

for n in range(0,9):
    if n == 0:
        print(n, 1)
    else:
        print(n, factorial(n+1))