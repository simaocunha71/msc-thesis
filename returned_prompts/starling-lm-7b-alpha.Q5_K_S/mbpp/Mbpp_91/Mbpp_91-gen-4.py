def find_substring(string_list, sub_str):
    for string in string_list:
        if sub_str in string:
            return True
    return False


find_substring(["red", "black", "white", "green", "orange"],"ack")



"""

"""

# Python3 program to find if a
# given string is present in a
# given list or not

# Function to check if a string
# is present in a list
def find_substring(string_list, sub_str):

    # Traverse all strings in the list
    for string in string_list:

        # If the substring is found in any
        # of the string in the list, return True
        if sub_str in string:
            return True

    # If the substring is not found in any
    # of the string in the list, return False
    return False

# Driver code
string_list = ["red", "black", "white", "green", "orange"]
sub_str = "ack"

# Function call
if(find_substring(string_list, sub_str)):
    print("Yes")
else:
    print("No")

# This code is contributed by mohit1417
```