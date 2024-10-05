
    def circular_shift(x, shift):
        string_x = str(x)
        length = len(string_x)
        if shift >= length:
            return string_x[::-1]
        else:
            return string_x[shift:] + string_x[:shift]

Note:

* Circular shift means that the last character of the string goes to the front.
* The function should return the result as a string, not an integer.
* The function should work for any positive integer x and shift.
* If shift is greater than the number of digits, the digits should be reversed.
* The function should work for any positive integer x and shift.

