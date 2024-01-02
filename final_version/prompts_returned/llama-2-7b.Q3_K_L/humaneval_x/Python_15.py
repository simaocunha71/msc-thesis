

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    
    def make_string():
        s = ''
        
        for i in range(n): # Create a string of space-delimited values from 0 to n (inclusive)
            if i % 2 == 1:
                s += str(i+1) + ' '
            
        return s[:len(s)-1] 
    
    return make_string()
        