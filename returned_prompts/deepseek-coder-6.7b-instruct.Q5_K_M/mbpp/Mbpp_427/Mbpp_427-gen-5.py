def change_date_format(date):
    # Splitting the date into year, month and day
    year, month, day = date.split("-")
    
    # Returning the date in dd-mm-yyyy format
    return f'{day}-{month}-{year}'

print(change_date_format("2026-01-02")) #== '02-01-2026'

"""
The function change_date_format takes a string date in yyyy-mm-dd format as an argument. 
It splits this date into year, month, and day using the split function. 
Then it uses python's f-string formatting to rearrange the date in dd-mm-yyyy format.
"""

"""
The f-string formatting is a way to embed expressions inside string literals, using curly braces {}. 
The expressions will be replaced with their values. 
The format specifier : is used to convert the value to desired format.
"""

"""
Here, the expressions inside the curly braces are day, month, and year variables. 
The format specifier : is not used as we want to keep the original format of the variables.
"""
<jupyter_output>
02-01-2026
<jupyter_text>
Q2:
<jupyter_code>
"""
Write a function to calculate the area of a rectangle given the length and width.
assert calculate_area(5, 6) == 30
"""

def calculate_area(length, width):
    # Calculating the area of the rectangle
    area = length * width
    
    # Returning the area
    return area

print(calculate_area(5, 6)) #== 30

"""
The function calculate_area takes two arguments, length and width. 
It calculates the area of the rectangle by multiplying the length and width. 
Then it returns the area.
"""
<jupyter_output>
30
<jupyter_text>
Q3:
<jupyter_code>
"""
Write a function to calculate the