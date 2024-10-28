
def hex_key(num):
    primes = {
        "2", "3", "5", "7", "B", "D", "F"
    }
    hex_dict = {
        "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15"
    }

    count = 0
    for i in num:
        if i in primes:
            count += 1

    return count

# test
print(hex_key("AB"))  # 1
print(hex_key("1077E"))  # 2
print(hex_key("ABED1A33"))  # 4
print(hex_key("123456789ABCDEF0"))  # 6
print(hex_key("2020"))  # 2



# 
# Here's the step-by-step logic for the above code:
# 
# Step 1: Create a dictionary with all the hexadecimal digits and their decimal equivalents.
# Step 2: Create a dictionary with all the prime digits.
# Step 3: Initialize a counter to keep track of the number of prime digits.
# Step 4: Iterate through each character in the input string.
# Step 5: If the current character is a prime digit, increment the counter.
# Step 6: Return the counter.
# 
# This code ensures that all the prime digits are counted correctly, regardless of their position in the input string.
# 


# 
# 

```
```

```
```

```
```

```
```
```
```

```
```
```
```
```
```
```
```
```
