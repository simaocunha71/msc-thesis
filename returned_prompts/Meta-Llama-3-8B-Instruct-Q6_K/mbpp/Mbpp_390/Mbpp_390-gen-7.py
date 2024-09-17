```
def add_string(lst, format_string):
    return [format_string.format(i) for i in lst]
```



This function uses a list comprehension to iterate over each element in the input list. For each element, it uses the format method of the format string to create a new string with the element inserted at the specified position. The resulting list of strings is then returned. 

The unit test provided ensures that this function works correctly, as it checks that the function correctly applies the format string to each element in the input list. 

For example, if the input list is [1, 2, 3, 4] and the format string is 'temp{0}', the function will return ['temp1', 'temp2', 'temp3', 'temp4']. 

This function can be used to apply a variety of formats to a list of elements, such as inserting the elements into a string, formatting the elements as numbers or dates, or even applying a function to each element. 

The format string used in this function is a placeholder for the element to be inserted. The {0} in the format string represents the first element in the list, {1} represents the second element, and so on. The format method replaces these placeholders with the actual elements from the list. 

This function is a flexible and powerful tool for manipulating lists of data, and can be used in a wide range of applications. 

Here is the unit test provided:
```
assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
```



And here is the function:
```
def add_string(lst, format_string):
    return [format_string.format(i) for i in lst]
```



This function can be used to apply a given format string to all of the elements in a list. It is a flexible and powerful tool for manipulating lists of data, and can be used in a wide range of applications. 

For example, if you have a list of numbers and you want to convert them to strings and add a prefix to each string, you can use this function. 

You can also use this function to apply a function to each element in the list. For example, if you have a list of numbers and you want to square each number, you can use this function in combination with the built-in map function. 

This function is a valuable addition to any programmer's toolkit, and can be used to solve a