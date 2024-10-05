def fruit_distribution(s,n):
    total_apples, total_oranges = map(int, re.findall(r'\d+', s))
    return n - total_apples - total_oranges

print(fruit_distribution("5 apples and 6 oranges", 19)) # 8
print(fruit_distribution("0 apples and 1 oranges",3)) # 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # 95
print(fruit_distribution("100 apples and 1 oranges",120)) # 19