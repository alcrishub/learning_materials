def full_email(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_email([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))
