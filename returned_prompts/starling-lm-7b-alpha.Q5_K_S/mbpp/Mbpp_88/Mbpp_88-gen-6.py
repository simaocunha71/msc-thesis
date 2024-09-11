```
def freq_count(lst):
    count_dict = {}
    for i in lst:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict
```

Explanation:
The function `freq_count` takes a list as input and returns a dictionary of the frequencies of each element in the list. It does this by iterating through each element in the list. If the element is already in the dictionary, it increments the count. Otherwise, it adds the element to the dictionary with a count of 1.

To test the function, you can use the `assert` statement to check if the result of `freq_count` on the provided list `[10,10,10,10,20,20,20,20,40,40,50,50,30]` is equal to the expected dictionary `{10: 4, 20: 4, 40: 2, 50: 2, 30: 1}`.

This function provides a straightforward way to count the frequency of elements in a list and can be easily extended to handle larger lists or more complex scenarios if needed.

Python is a versatile programming language that has a wide range of applications, from web development to data analysis and machine learning. Its simplicity and readability make it a popular choice for beginners and experienced programmers alike.

Here are some key features of Python:

1. Readability and simplicity: Python is known for its clear syntax and easy-to-read code. This makes it a great language for beginners to learn and for experienced programmers to quickly understand and work with code.

2. Extensive standard library: Python comes with a comprehensive standard library that provides a wide range of functionalities, from string manipulation to network programming. This makes it easy to solve many common programming tasks without having to write additional code.

3. Extensibility: Python can be easily extended with C or C++ code, allowing you to leverage the performance of these languages when needed.

4. Cross-platform compatibility: Python is available for multiple platforms, including Windows, macOS, and Linux. This makes it a great