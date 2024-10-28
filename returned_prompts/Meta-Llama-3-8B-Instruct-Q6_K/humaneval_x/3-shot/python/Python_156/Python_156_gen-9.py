    roman_numerals = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l',
        90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
    }

    def int_to_roman(num):
        roman = ''
        for value, numeral in sorted(roman_numerals.items(), reverse=True):
            while num >= value:
                roman += numeral
                num -= value
        return roman.lower()

    return int_to_roman(number) if 1 <= number <= 1000 else ''
    # This code is not complete, it's just a skeleton and will not work
    # You need to implement the int_to_roman function and use it here.
    # The int_to_roman function should take an integer as input and return its roman numeral equivalent as a string in lowercase.
    # You can use the roman_numerals dictionary to help you with the conversion.  # You can use a while loop to convert the number to roman numerals.  # You should handle the cases for 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000 separately.  # You should return the roman numeral as a string in lowercase.  # You can test your code with the provided examples.  # You should handle the case where the input number is outside the range 1-1000.  # You can use a try-except block to handle this.  # You can raise a ValueError with a suitable message.  # You should test your code with the provided examples.  # You can use the assert statement to test your code.  # You can use the print statement to print the result of your code.  # You can use the input statement to get the input from the user.  # You can use the sys module to handle the case where the input is not a valid integer.  # You can use the try-except block to handle this.  # You can raise a ValueError with a suitable message.  # You should test your code with the provided examples.  # You can use the assert statement to test your code.  # You can use the print statement to