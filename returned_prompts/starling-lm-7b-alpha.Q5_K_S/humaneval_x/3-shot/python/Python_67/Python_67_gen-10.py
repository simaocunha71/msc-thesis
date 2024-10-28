    fruits = ["apples","oranges"]
    total_fruits = n
    mangos = 0
    for fruit in fruits:
        total_fruits -= s.count(fruit)
    return total_fruits


