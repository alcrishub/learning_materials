set_numbers = [1, 2, 4, 3, 6, 5, 8, 9, 10, 11, 12, 0]
for x in set_numbers:
    for y in set_numbers:
        if x + y == 11:
            print("{} + {} = 11".format(x, y))
