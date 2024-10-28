    apples = int(fruit_distribution("5 apples and 6 oranges", 19).split("apples")[0])
    oranges = int(fruit_distribution("5 apples and 6 oranges", 19).split("oranges")[0])
    return n - apples - oranges