def occurance_substring(main_str, sub_str):
    i = main_str.find(sub_str)
    if i == -1:
        return None
    else:
        return (sub_str, i, i + len(sub_str))

# Driver code
print(occuarance_substring('python programming, python language','python'))



"""
Explanation:
The function `occuarance_substring` takes in two arguments: `main_str` and `sub_str`. It uses the `find` method of strings to search for the `sub_str` within the `main_str`. If the `sub_str` is not found, the `find` method returns -1, and the function returns `None`. Otherwise, it returns a tuple containing the `sub_str`, the index at which it is found in the `main_str`, and the index at which it ends in the `main_str`.
"""







"""
Explanation:
The function `occuarance_substring` takes in two arguments: `main_str` and `sub_str`. It uses a while loop to continuously find the next occurrence of the `sub_str` within the `main_str` by starting the search from the index immediately following the previous occurrence. It uses the `find` method of strings to search for the `sub_str` within the `main_str`. If the `sub_str` is not found, the `find` method returns -1, and the function returns `None`. Otherwise, it returns a tuple containing the `sub_str`, the index at which it is found in the `main_str`, and the index at which it ends in the `main_str`. The function continues to find and return occurrences of the `sub_str` until no more occurrences are found.
"""



"""
Explanation:
The function `occuarance_substring` takes in two arguments: `main_str` and `sub_str`. It uses a while loop to continuously find the next occurrence of the `sub_str` within the `main_str` by starting the search from the index immediately following the previous occurrence. It uses the `find` method of strings to search for the `sub_str` within the