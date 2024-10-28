    fruits = s.split(" ")[0]
    fruits = fruits.split(" ")
    fruits_list = []
    for i in fruits:
        fruits_list.append(int(i.split(" ")[1]))
    n = int(n)
    return n - sum(fruits_list)


