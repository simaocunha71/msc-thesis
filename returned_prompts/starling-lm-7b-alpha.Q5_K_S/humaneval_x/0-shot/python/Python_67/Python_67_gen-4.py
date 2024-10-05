
def fruit_distribution(s,n):
    temp_list = s.split(" ")
    apples = int(temp_list[0].split(" ")[-1])
    oranges = int(temp_list[1].split(" ")[-1])
    total_fruits = int(temp_list[0].split(" ")[0]) + int(temp_list[1].split(" ")[0])
    mangos = n - total_fruits
    return mangos

print(fruit_distribution("5 apples and 6 oranges", 19)) #19 - 5 - 6 = 8
print(fruit_distribution("0 apples and 1 oranges",3)) #3 - 0 - 1 = 2
print(fruit_distribution("2 apples and 3 oranges", 100)) #100 - 2 - 3 = 95
print(fruit_distribution("100 apples and 1 oranges",120)) #120 - 100 - 1 = 19






```
