    fruits = s.split(' and ')
    fruits = [int(fruit.split(' ')[1]) for fruit in fruits]
    total = n
    for fruit in fruits:
        total -= fruit
    return total


