
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    for char in string:
        if char.isalnum() or \
            (char == '-' and len(string) == 1):
            #print "removing %c" % char
            continue
        else:
            return False

    return True

prime_length('Hello')
```