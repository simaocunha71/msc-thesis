def remove_Occ(string,char):
    char_count = 0
    for i in range(len(string)):
        if(string[i] == char):
            char_count += 1
    if(char_count > 1):
        string = string[0:i+1] + string[i+1:-1*char_count] + string[len(string)-char_count:]
    return string

# Testing the function
assert remove_Occ("hello","l") == "heo"
print("Test Passed!")



# Another Approach
def remove_Occ_2(string, char):
    return string.replace(char, '', 2)

# Testing the function
assert remove_Occ_2("hello", "l") == "heo"
print("Test Passed!")



# Another Approach
def remove_Occ_3(string, char):
    while string.count(char) > 2:
        string = string.replace(char, '', 1)
    return string

# Testing the function
assert remove_Occ_3("hello", "l") == "heo"
print("Test Passed!")



# Another Approach
def remove_Occ_4(string, char):
    while string.count(char) > 2:
        string = string.replace(char, '', 1)
    return string

# Testing the function
assert remove_Occ_4("hello", "l") == "heo"
print("Test Passed!")



# Another Approach
def remove_Occ_5(string, char):
    while string.count(char) > 2:
        string = string.replace(char, '', 1)
    return string

# Testing the function
assert remove_Occ_5("hello", "l") == "heo"
print("Test Passed!")


"""
Test Cases:
remove_Occ("hello","l") == "heo"
remove_Occ("hallo","l") == "hao"
remove_Occ("world","o") == "wrld"
remove_Occ("hello","e") == "hll