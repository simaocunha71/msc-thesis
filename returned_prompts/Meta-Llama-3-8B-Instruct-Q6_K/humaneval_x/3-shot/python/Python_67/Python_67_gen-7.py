    s = s.replace("apples and", " ")
    s = s.replace("oranges", " ")
    fruits = s.split()
    return int(fruits[0]) - int(fruits[1]) - int(fruits[2]) + n


