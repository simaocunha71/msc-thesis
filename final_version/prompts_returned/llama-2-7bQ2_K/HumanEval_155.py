
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if not num:
        return None, None

    evenDigits = 0
    oddDigits = 0
    
    while True: # break on negative numbers or evenDigit == 10
        digit = int(num / 10)
        
        if digit == -1:
            break
        
        evenDigit = int(num % 10)
        oddDigits += (evenDigit in [2, 4, 6, 8])
        num = str(digit * 10) + str(evenDigit)
    return evenDigits, oddDigits
