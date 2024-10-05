    n = int(n)
    fruit_list = s.split(" ")
    apple = int(fruit_list[0][2:])
    orange = int(fruit_list[1][0:len(fruit_list[1])-1])
    total = apple + orange
    return n - total


