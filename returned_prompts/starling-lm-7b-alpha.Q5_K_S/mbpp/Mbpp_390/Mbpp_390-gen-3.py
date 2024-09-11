"""
def add_string(l,s):
    return [s.format(i) for i in l]
"""

def add_string(l,s):
    return [s.format(i) for i in l]



def test_add_string():
    assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
    print("All tests passed.")


if __name__ == "__main__":
    test_add_string()



```
In this code, the function add_string takes in a list and a format string as parameters. It uses a list comprehension to iterate over each element in the input list, and for each element, it applies the format string using the .format() method. The result is a new list with the format string applied to each element. The assert statement at the end of the code checks if the function is working correctly by comparing the result of add_string with the expected output.
```