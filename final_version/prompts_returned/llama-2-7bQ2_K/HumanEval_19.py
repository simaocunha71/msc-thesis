from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    numberals = [x.strip() for x in numbers.split(' ')] # Convert spaces into newlines
    digit_list = []   # This is a list of digits from 0 to 9, sorted ascendingly
    while len(numberals) > 0:
        numberal = str(int(numberals[0])+1).zfill(len(str(int(numberals[0])))) + numberals[0]   # add the digit and a space to the front of numbers from 'zero' to 'nine'
        if len(digit_list) > 0:                                                # If digit list isn't empty yet...
            digit_list[-1] += numberal                    # Add the new digit to the end of the digit list
        else:                                               # Otherwise...
            digit_list.append(' '+numberal)             # Add the new digit and a space to the front of the digits list
        numberals = [str(x).zfill(10) for x in sorted(digit_list, key=lambda x: x[0])][-1:-5]      # Remove the leading zeros and sort
    print(numberals)        
    return ' '.join([''.join([str(int(d))+('0' if d else '')]) for d in numberals[:6]])     # Add a '0' before every 2nd digit except the first one, which is already sorted