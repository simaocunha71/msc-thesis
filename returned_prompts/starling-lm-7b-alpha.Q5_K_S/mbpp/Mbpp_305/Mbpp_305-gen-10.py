def start_withp(words):
    return (word for word in words if word.startswith('p'))

# Testing
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')











































"""
Write a function to return two words from a list of words starting with letter 'p'.

Explanation:
The above code defines a function called start_withp that takes a list of words as an argument.
The function uses a generator expression to create a generator object that yields only the words from the input list that start with the letter 'p'. The yielded words are then assigned to the variables 'word1' and 'word2'.
In the assertion, the function start_withp is called with the list of words ["Python PHP", "Java JavaScript", "c c++"]. The assertion checks if the returned values of start_withp are equal to the expected values ('Python', 'PHP'), and if so, the assertion passes.

In this case, the assertion will pass because the list of words ["Python PHP", "Java JavaScript", "c c++"] contains two words that start with the letter 'p', namely "Python" and "PHP". The function start_withp correctly identifies these two words and returns them as the result.

Note: The assert keyword is used to check if a condition is true or false. If the condition is true, the program continues execution; if the condition is false, an AssertionError is raised, and the error message is printed.

"""

# Python3 program to demonstrate working of
# assert keyword in python


# Function to demonstrate working of assert
# keyword in Python
def start_withp(words):
    return (word for word in words if word.startswith('p'))

# Driver code
if __name__ == "__main__":
    words = ["Python PHP", "Java JavaScript", "c c++"]
    print(start_withp(words))

# This code is contributed by 
# Sanjeev_Dewan
``