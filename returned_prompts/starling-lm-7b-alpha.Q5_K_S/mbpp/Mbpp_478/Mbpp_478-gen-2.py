def remove_lowercase(s):
    return "".join(c for c in s if c.isupper())


print(remove_lowercase("PYTHon"))


# Explanation:
# The function remove_lowercase takes a string s as input and uses a generator expression to create a new string that only contains uppercase characters. The function then returns this new string.
# The generator expression (c for c in s if c.isupper()) iterates over each character c in the input string s. The if statement c.isupper() checks if the character is uppercase, and if so, includes it in the generator expression. The "".join() method is used to join all the included characters together into a new string.
# Finally, the function print(remove_lowercase("PYTHon")) is used to test the function by removing lowercase substrings from the input string "PYTHon" and printing the result "PYTH".

# Here are some additional notes on the code:
# The function remove_lowercase is defined with the def keyword, indicating that it is a user-defined function. It takes one parameter, s, which represents the input string.
# The return statement is used to specify the value that the function should return. In this case, it returns the new string created by the "".join() method.
# The if statement c.isupper() is used to check if a character is uppercase. The isupper() method is a built-in method in Python that returns True if the character is uppercase, and False otherwise.
# The "".join() method is a string method in Python that joins a sequence of characters into a new string. In this case, it joins all the included uppercase characters from the generator expression into a new string.
# The print() function is used to print the result of the function call remove_lowercase("PYTHon"). It takes one argument, the value to be printed, and outputs it to the console.

# Overall, this code demonstrates a simple and efficient way to remove lowercase substrings from a given string using a generator expression and the "".join() method.










































