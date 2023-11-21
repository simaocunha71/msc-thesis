
def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """

    db = 'db'
    binary_string = []
    
    while decimal > 0:
        if int(decimal/2) > 1:
            binary_string.append('1')
        else:
            binary_string.append('0')
        decimal -= (int(decimal / 2))
        
    return binary_string + db*3

#Declaring and defining variables globally.
a = int(input("Enter a number to convert in Decimal To Binary : "))
b = decimal_to_binary(a)
print(a,"\n",b)