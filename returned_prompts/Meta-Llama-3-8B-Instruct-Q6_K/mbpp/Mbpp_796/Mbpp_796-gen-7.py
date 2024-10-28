```
def return_sum(d):
    return sum(d.values())
```


This function uses the built-in sum function to add up all the values in the dictionary. The values method returns a view object that displays a list of all values in the dictionary. The sum function then adds up these values and returns the total. 

For example, if the dictionary is {'a': 100, 'b':200, 'c':300}, the function would return 600, which is the sum of these three values. 

The unit test `assert return_sum({'a': 100, 'b':200, 'c':300}) == 600` ensures that the function is working correctly. It checks that the function returns 600 when given the dictionary {'a': 100, 'b':200, 'c':300}. If the function is working correctly, the unit test will pass. If the function is not working correctly, the unit test will fail, indicating that there is an error in the function. 

This function can be used with any dictionary, not just the one provided in the unit test. It is a general solution that can be applied to any dictionary. 