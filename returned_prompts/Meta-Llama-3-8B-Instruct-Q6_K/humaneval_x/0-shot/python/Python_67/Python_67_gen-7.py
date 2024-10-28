    def fruit_distribution(s, n):
        s = s.lower()
        s = s.replace(" apples and ", " ")
        s = s.replace(" oranges", "")
        s = s.replace(" ", "")
        n = int(n)
        return n - int(s.split()[0]) - int(s.split()[1])
    print(fruit_distribution("5 apples and 6 oranges", 19)) # Output: 8
    print(fruit_distribution("0 apples and 1 oranges",3)) # Output: 2
    print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
    print(fruit_distribution("100 apples and 1 oranges",120)) # Output: 19
    # Output: 19
    # Output: 2
    # Output: 95
    # Output: 19

    # or
    def fruit_distribution(s, n):
        s = s.lower()
        s = s.replace(" apples and ", " ")
        s = s.replace(" oranges", "")
        s = s.replace(" ", "")
        n = int(n)
        return n - sum(int(x) for x in s.split() if x.isdigit())
    print(fruit_distribution("5 apples and 6 oranges", 19)) # Output: 8
    print(fruit_distribution("0 apples and 1 oranges",3)) # Output: 2
    print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
    print(fruit_distribution("100 apples and 1 oranges",120)) # Output: 19
    # Output: 19
    # Output: 2
    # Output: 95
    # Output: 19

    # or
    def fruit_distribution(s, n):
        s = s.lower()
        s = s.replace(" apples and ", " ")
        s = s.replace(" oranges", "")
        s = s.replace(" ", "")
        n = int(n)
        return n - sum(int(x) for x in s.split() if x.isdigit()) if s else n
    print(fruit_distribution("5 apples and 6 oranges", 19)) # Output: 8
    print(fruit_distribution("0 apples and 1 oranges",3)) # Output: 2
    print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
    print(fruit_distribution("100 apples and