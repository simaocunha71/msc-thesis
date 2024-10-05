    result = []
    for elem in numbers:
        if elem not in result:
            result.append(elem)
    return result




# Programming questions related to Python
# Python is an interpreted, high-level, general-purpose programming language. Python's design philosophy emphasizes code readability, and a syntactical reduction that will permit writing programs in fewer lines of code than would be possible in languages such as C++ or Java.
# It supports multiple programming paradigms, including object-oriented, imperative and functional programming or procedural styles. It features dynamic typing and garbage collection, and uses the indentation to delimit blocks, enhancing code readability.
# Python was created by Guido van Rossum and first released in 1991. Python 2.0, with the addition of generators and list comprehensions, was released in October 2000. In December 2008, Python 3.0 was released, with significant syntax changes to the language.

# Here are some Python related questions:
# 1. What are the key features of Python programming language?
# Python's design philosophy emphasizes code readability, and a syntactical reduction that will permit writing programs in fewer lines of code than would be possible in languages such as C++ or Java. It supports multiple programming paradigms, including object-oriented, imperative and functional programming or procedural styles. It features dynamic typing and garbage collection, and uses the indentation to delimit blocks, enhancing code readability.

# 2. How can I create a Python program to remove all elements that occur more than once from a list of integers, keeping the order of the remaining elements the same as in the input?
# You can use the remove_duplicates function provided in the question. Here's an example usage:

numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

# This function iterates over the input list, and for each element, it checks if it is already present in the result list. If not, it appends the element to the result list. This way, it ensures that only unique elements are kept in the result list, while