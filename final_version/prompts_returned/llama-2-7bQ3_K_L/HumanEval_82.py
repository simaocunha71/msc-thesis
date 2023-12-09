
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    
    if len(string) < 2:
        return False

    list_of_numbers = []
    for c in string:
        if str(c).isdigit(): # check if the character is a number, if it is a number then add to our list of numbers
            list_of_numbers.append(int(c))
            
    prime = True
    
    while prime == True:
        sum = 0
        
        for i in range(2, len(list_of_numbers)): # keep iterating through the list until you get to the second number in our list of numbers
            if (list_of_numbers[i] % list_of_numbers[i-1]) == 0: # check if the previous number is a multiple of the current one
                prime = False
                
        sum += list_of_numbers[len(list_of_numbers)]
        del list_of_numbers[-1]
        
    return True if len(sum) > 2 else False