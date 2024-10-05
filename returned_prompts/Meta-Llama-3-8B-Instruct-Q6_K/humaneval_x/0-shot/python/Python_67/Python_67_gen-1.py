    def fruit_distribution(s, n):
        s = s.replace(" apples and ", " ")
        s = s.replace(" oranges", "")
        s = s.replace(" apples", "")
        total_fruits = int(s)
        apples = 0
        oranges = 0
        for word in s.split():
            if word.isdigit():
                total_fruits = int(word)
            elif word == "apples":
                apples = int(s.split("apples")[0].strip().replace(" ", ""))
            elif word == "oranges":
                oranges = int(s.split("oranges")[0].strip().replace(" ", ""))
        return total_fruits - apples - oranges

# testing the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # output: 8
print(fruit_distribution("0 apples and 1 oranges",3))  # output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # output: 95
print(fruit_distribution("100 apples and 1 oranges",120))  # output: 19
print(fruit_distribution("1 apples", 1))  # output: 0
print(fruit_distribution("1 oranges", 1))  # output: 0
print(fruit_distribution("1 apples and 1 oranges", 2))  # output: 0
print(fruit_distribution("10 apples and 10 oranges", 20))  # output: 0
print(fruit_distribution("1 apple and 1 orange", 2))  # output: 0
print(fruit_distribution("100 apples and 100 oranges", 200))  # output: 0
print(fruit_distribution("1 apple and 2 oranges", 3))  # output: 0
print(fruit_distribution("2 apples and 1 orange", 3))  # output: 0
print(fruit_distribution("1 apple and 3 oranges", 4))  # output: 0
print(fruit_distribution("3 apples and 1 orange", 4))  # output: 0
print(fruit_distribution("1 apple and 4 oranges", 5))  # output: 0
print(fruit_distribution("4 apples and 1 orange", 5))  # output: 0
print(fruit_distribution("1 apple and 5 oranges", 6))  # output: 0
print(fruit_distribution