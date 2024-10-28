    # Split the string into a list of words
    words = s.split()
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over each word in the list of words
    for word in words:
        # Initialize a counter for consonants
        consonant_count = 0
        
        # Iterate over each character in the word
        for char in word:
            # Check if the character is a consonant
            if char.lower() not in 'aeiou':
                # If the character is a consonant, increment the counter
                consonant_count += 1
        
        # Check if the word contains exactly n consonants
        if consonant_count == n:
            # If it does, add the word to the result list
            result.append(word)
    
    # Return the result list
    return result
# Test the function
print(select_words("Mary had a little lamb", 4))  # Output: ["little"]
print(select_words("Mary had a little lamb", 3))  # Output: ["Mary", "lamb"]
print(select_words("simple white space", 2))  # Output: []
print(select_words("Hello world", 4))  # Output: ["world"]
print(select_words("Uncle sam", 3))  # Output: ["Uncle"]


