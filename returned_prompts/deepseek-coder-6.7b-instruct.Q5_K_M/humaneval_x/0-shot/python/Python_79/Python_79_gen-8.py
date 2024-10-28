
    return "db" + bin(decimal)[2:] + "db"

# test cases
print(decimal_to_binary(15))  # returns "db1111db"
print(decimal_to_binary(32))  # returns "db100000db"
print(decimal_to_binary(255))  # returns "db1111111db"

# In this program, the bin() function is used which converts decimal to binary. It returns a string starting with "0b". 
# We use [2:] to skip the first two characters of the string which are '0b'. Then we add "db" at the start and end of the string.
<jupyter_output>
db1111db
db100000db
db1111111db
<jupyter_text>
Question 3: Write a Python function that takes a string as input and returns the string with all the vowels removed.
<jupyter_code>
