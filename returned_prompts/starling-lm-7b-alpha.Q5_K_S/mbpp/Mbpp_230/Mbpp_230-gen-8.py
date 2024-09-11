def replace_blank(s,c):
    return s.replace(' ' , c)


# Another Solution
def replace_blank(s,c):
    return s.replace(' ' , c)

# Testing the function
assert replace_blank("hello people",'@') == "hello@people"
print("All tests passed")


# Testing the function
assert replace_blank("This is a test string",'%') == "This is a %test string"
print("All tests passed")

# Testing the function
assert replace_blank("This is a test string with blank spaces",'%') == "This is a test string with %test spaces"
print("All tests passed")

# Testing the function
assert replace_blank("",'%') == ""
print("All tests passed")

# Testing the function
assert replace_blank("This is a test string with no blank spaces",'%') == "This is a test string with no blank spaces"
print("All tests passed")


# Testing the function
assert replace_blank("This is a test string with multiple blank spaces",'%') == "This is a test string with multiple %test spaces"
print("All tests passed")


# Testing the function
assert replace_blank("This is a test string with leading and trailing blank spaces",'%') == "This is a test string with leading and trailing %test spaces"
print("All tests passed")


# Testing the function
assert replace_blank("This is a test string with leading and trailing blank spaces with a single blank space in between",'%') == "This is a test string with leading and trailing %test spaces with a single blank space in between"
print("All tests passed")


# Testing the function
assert replace_blank("This is a test string with leading and trailing blank spaces with a single blank space in between and a double blank space at the end",'%') == "This is a test string with leading and trailing %test spaces with a single blank space in between and a double %test space at the end"
print("All tests passed")


# Testing the function
assert replace_blank("This is a test string with leading and trailing blank spaces with a single blank space in between and a