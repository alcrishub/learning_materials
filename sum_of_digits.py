def digitAdder(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    if sum//10 > 0:
        digitAdder(sum)
    else:
        print(sum)
        
digitAdder(12345678)
