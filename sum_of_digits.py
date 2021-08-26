sum = 0
new_sum = 0
x = 99999499
for digit in str(x):
    sum += int(digit)
print(sum)
if sum/10 > 0:
    for digit in str(sum):
        new_sum += int(digit)
    print(new_sum)
    