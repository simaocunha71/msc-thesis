    total_apples = int(s.split("apples")[0])
    total_oranges = int(s.split("oranges")[0].split("and")[1])
    total_fruits = n
    return total_fruits - total_apples - total_oranges

