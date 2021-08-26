def car_listing(car_prices):
    result = ""
    for a in car_prices.keys():
        result += "{0} costs {1} dollars".format(a,car_prices[a]) + "\n"
    return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))