
    def closest_integer(value):
        '''
        Create a function that takes a value (string) representing a number
        and returns the closest integer to it. If the number is equidistant
        from two integers, round it away from zero.
        '''
        num = float(value)
        if num > 0:
            return int(num + 0.5)
        else:
            return int(num - 0.5)

    return closest_integer(value)

print(closest_integer("10"))
print(closest_integer("15.3"))
print(closest_integer("14.5"))
print(closest_integer("-14.5"))

'''
The function closest_integer takes a string value and converts it to a float.
If the float is positive, it adds 0.5 before converting to an integer,
which rounds up the number. If the float is negative, it subtracts 0.5 before 
converting to an integer, which rounds down the number.
'''

# 4. Write a Python function that checks whether a string is a valid IPv4 address.

