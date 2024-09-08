def reverse_words(s):
    # Split the string into a list of words
    words = s.split()
    
    # Reverse the list of words
    words.reverse()
    
    # Join the reversed list of words into a string
    reversed_s = ' '.join(words)
    
    return reversed_s