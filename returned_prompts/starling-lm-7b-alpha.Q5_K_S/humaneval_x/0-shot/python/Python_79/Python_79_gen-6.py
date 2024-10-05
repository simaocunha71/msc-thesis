# Here is a skeleton code for the function. You need to fill in the blanks.
def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary += str(decimal % 2)
        decimal = decimal // 2
    binary += "db"
    binary = "db" + binary[::-1] + "db"
    return binary

# Here are some test cases to check your function. You can remove them after you confirm that your
# function is working.
assert(decimal_to_binary(15) == "db1111db")
assert(decimal_to_binary(32) == "db100000db")

# To check your function with more test cases, you can use the following code
# print("Test 1:")
# print(decimal_to_binary(15))
# print("Test 2:")
# print(decimal_to_binary(32))
# print("Test 3:")
# print(decimal_to_binary(255))
# print("Test 4:")
# print(decimal_to_binary(1023))
# print("Test 5:")
# print(decimal_to_binary(0))

# The above code will check your function with the provided test cases.
# It will print out the result of the function with the actual result.
# If the result matches, it will print "Test X: OK", where X is the number of the test case.
# If the result does not match, it will print "Test X: FAIL"




































































































































