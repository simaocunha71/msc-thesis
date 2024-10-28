    s = s.replace("apples and", "apples ").replace("oranges", "oranges ").split()
    total_apples = int(s[0].replace("apples", ""))
    total_oranges = int(s[2].replace("oranges", ""))
    total_fruits = int(n)
    return total_fruits - total_apples - total_oranges
    



