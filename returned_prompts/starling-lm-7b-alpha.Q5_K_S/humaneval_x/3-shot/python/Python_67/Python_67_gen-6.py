    fruit = ["apples", "oranges", "mangoes"]
    num = s.split(" ")
    num_list = []
    for i in num:
        num_list.append(int(i.split(" ")[-1]))
    total_fruit = sum(num_list)
    return total_fruit - sum(num_list[:2])


