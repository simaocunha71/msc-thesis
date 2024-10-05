    # Convert to list so we can modify the index
    numerals = list(str(number))
    # Initialize the roman numeral string
    result = ""
    # Go through each number in the list
    for i in range(len(numerals)):
        # Initialize the current numeral
        current_numeral = ""
        # Go through each roman numeral
        for j in range(10, 0, -1):
            # Go through each number 0-9
            for k in range(j):
                # If the number is larger than the current numeral
                if k > int(numerals[i]):
                    # Add the roman numeral to the current numeral
                    current_numeral += roman_numerals[j][k]
                    # Break the loop
                    break
            # If the number is equal to the current numeral, break the loop
            if k == int(numerals[i]):
                break
        # Add the current numeral to the result string
        result += current_numeral
    # Return the result string
    return result

roman_numerals = {
    1000: "m",
    900: "cm",
    500: "d",
    400: "cd",
    100: "c",
    90: "xc",
    50: "l",
    40: "xl",
    10: "x",
    9: "ix",
    5: "v",
    4: "iv",
    1: "i",
}

# Test the function
print(int_to_mini_roman(19))  # "xix"
print(int_to_mini_roman(152))  # "clii"
print(int_to_mini_roman(426))  # "cdxxvi"

# Stretch: Create a function that takes a string of roman numerals and
# converts it to an integer.

def mini_roman_to_int(roman_numerals):
    """
    Given a string of roman numerals, obtain its integer equivalent,
   