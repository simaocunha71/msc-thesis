    apples = int(s.split("apples")[0])
    oranges = int(s.split("oranges")[0].split("and")[1])
    total_fruits = n
    mangoes = total_fruits - apples - oranges
    return mangoes

