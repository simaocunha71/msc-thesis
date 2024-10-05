
def fruit_distribution(s,n):
    s = s.split()
    a = int(s[0][-1])
    b = int(s[2][-1])
    c = n - (a + b)
    return c



# fruit_distribution("5 apples and 6 oranges", 19)
# fruit_distribution("0 apples and 1 oranges",3)
# fruit_distribution("2 apples and 3 oranges", 100)
# fruit_distribution("100 apples and 1 oranges",120)






```

The fruit_distribution function takes a string and an integer as input. The string represents a number of apples and oranges distributed in a basket of fruits. The integer represents the total number of fruits in the basket. The function splits the string to separate the number of apples and oranges, and then subtracts these values from the total number of fruits to find the number of mango fruits in the basket. The result is returned as the output of the function.

For example, if the function is called with the string "5 apples and 6 oranges" and the integer 19, the function will return 8, as there are 5 apples, 6 oranges, and 8 mango fruits in the basket.

The function uses string manipulation to extract the relevant information from the input string, and subtraction to calculate the number of mango fruits. It then returns the result as the output of the function.

Overall, the function provides a straightforward solution to the problem of finding the number of mango fruits in a basket given the total number of fruits and the number of apples and oranges.