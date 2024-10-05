    def fruit_distribution(s, n):
        s = s.lower()
        start = s.find("apples") + len("apples")
        end = s.find("and")
        if end == -1:
            end = len(s)
        apples = int(s[start:end].replace(" ", ""))
        start = s.find("oranges") + len("oranges")
        end = s.find("and", start) if s.find("and", start) != -1 else len(s)
        oranges = int(s[start:end].replace(" ", ""))
        return n - apples - oranges

# Testing the function
print(fruit_distribution("5 apples and 6 oranges", 19)) # Expected output: 8
print(fruit_distribution("0 apples and 1 oranges",3)) # Expected output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Expected output: 95
print(fruit_distribution("100 apples and 1 oranges",120)) # Expected output: 19
print(fruit_distribution("50 apples and 50 oranges", 150)) # Expected output: 50
print(fruit_distribution("10 apples and 20 oranges", 40)) # Expected output: 10
print(fruit_distribution("1 apple and 2 oranges", 3)) # Expected output: 0
print(fruit_distribution("0 apples and 0 oranges", 0)) # Expected output: 0
print(fruit_distribution("20 apples and 20 oranges", 50)) # Expected output: 10
print(fruit_distribution("1 apple and 1 orange", 3)) # Expected output: 1
print(fruit_distribution("100 apples and 100 oranges", 200)) # Expected output: 0
print(fruit_distribution("0 apples and 0 oranges", 10)) # Expected output: 10
print(fruit_distribution("20 apples and 20 oranges", 50)) # Expected output: 10
print(fruit_distribution("1 apple and 1 orange", 3)) # Expected output: 1
print(fruit_distribution("1 apple and 1 orange", 4)) # Expected output: 2
print(fruit_distribution("0 apples and 0 oranges", 5)) # Expected output: 5
print(fruit_distribution("1 apple and 1 orange", 6)) # Expected output: 4
print(fruit_distribution("0 apples and 0 oranges", 