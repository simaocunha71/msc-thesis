
    def fruit_distribution(s,n):
        apples = int(s.split()[0])
        oranges = int(s.split()[3])
        return n - apples - oranges

    print(fruit_distribution("5 apples and 6 oranges", 19))
    print(fruit_distribution("0 apples and 1 oranges",3))
    print(fruit_distribution("2 apples and 3 oranges", 100))
    print(fruit_distribution("100 apples and 1 oranges",120))

    # Output:
    # 8
    # 2
    # 95
    # 19

In this code, we first extract the number of apples and oranges from the given string. Then we subtract the number of apples and oranges from the total number of fruits to get the number of mangoes.
"""

# 2.
"""
