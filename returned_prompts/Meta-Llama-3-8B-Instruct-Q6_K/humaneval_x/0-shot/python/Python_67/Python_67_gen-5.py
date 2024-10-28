    # we will use the split function to split the string into two parts 
    # the first part is the number of apples and the second part is the number of oranges
    # then we will use the int function to convert the string into integer
    # finally we will subtract the number of apples and oranges from the total number of fruits

    # let's start with the function
    def fruit_distribution(s,n):
        # split the string into two parts
        s = s.split(" and ")
        # convert the string into integer
        apples = int(s[0].split()[0])
        oranges = int(s[1].split()[1])
        # subtract the number of apples and oranges from the total number of fruits
        return n - apples - oranges

    # test the function
    print(fruit_distribution("5 apples and 6 oranges", 19)) # output: 8
    print(fruit_distribution("0 apples and 1 oranges",3)) # output: 2
    print(fruit_distribution("2 apples and 3 oranges", 100)) # output: 95
    print(fruit_distribution("100 apples and 1 oranges",120)) # output: 19

