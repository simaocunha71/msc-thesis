
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """

    return str(number).zfill(3)[0:int(9-len(str(number)))]
    
def int_to_arabic(num):
    s = ''
    while num > 1:
        if (num % 2) == 1: # even number
            s+= str(num //2) + 'و'
        else:
            s+=str((num//2)+1) + 'و'
        num/=2
    return s[:-1]
    
def int_to_indian_numeral():
    """
    Given an integer, output it in the Indian numerals.
    Examples:
    >>> int_to_indian_numeral(1) == '५' # 5
    >>> int_to_indian_numeral(2) == '६' # 6
    >>> int_to_indian_numeral(3) == '७' # 7
    >>> int_to_indian_numeral(4) == '९' # 8
    >>> int_to_indian_numeral(5) == '३०/६०' # 50
    """
    if num == -1:
        return ""
    
    s = ''
    while num > 0:
            s += str(num //2) + 'ऋन्दीस़्/१ऋन्दीश/'
        num /= 2
    if num == -1:
        return ""
    
    return s[:-1