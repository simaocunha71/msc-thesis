def toggle_string(s):
    res = ''
    for c in s:
        if c.islower():
            res += c.upper()
        elif c.isupper():
            res += c.lower()
        else:
            res += c
    return res



def test_toggle_string():
    assert toggle_string("Python")==("pYTHON")
    assert toggle_string("Hello World")==("hELLO wORLD")
    assert toggle_string("12345")==("12345")
    assert toggle_string("hello, world!")==("HELLO, WORLD!")
    print("All tests passed.")


if __name__ == "__main__":
    test_toggle_string()




"""
The function toggle_string takes a string as input and returns a new string with all lowercase letters converted to uppercase, all uppercase letters converted to lowercase, and all other characters left unchanged.

The function uses a for loop to iterate through each character in the input string. It checks if the character is lowercase using the islower() method. If it is, it appends the uppercase version of the character to the result string using the upper() method. If the character is uppercase, it appends the lowercase version of the character using the lower() method. If the character is neither lowercase nor uppercase, it simply appends the character to the result string.

After iterating through all the characters in the input string, the function returns the result string.

The test_toggle_string function is used to test the toggle_string function with a few example inputs. It asserts that the output of toggle_string with the input "Python" is equal to the string "pYTHON". It then asserts that the output of toggle_string with the input "Hello World" is equal to the string "hELLO wORLD". Similarly, it asserts that the output of toggle_string with the input "12345" is equal to the string "12345". Finally, it asserts that the output of toggle_string with the input "hello, world!" is equal to the string "HELLO, WORLD!". If all the assert