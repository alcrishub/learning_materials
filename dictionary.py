file_counts = {"jpg":4, "txt":12, "py":22, "png": 6, "csv":9}
for ext, amount in file_counts.items():
    text = "There are {} files with the .{} extension".format(amount, ext)
    print(text)
for key in file_counts.keys():
    print(key, end=", ")
for value in file_counts.values():
    print(value, end=", ")