
def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    
    def is_vowel(c):
        return (48 in ord(c) or 65 in ord(c) or 90 in ord(c))  # Vowels are between "A" and "Z"
    
    def get_closest_vowel(word, pos=1):
        """return vowel between pos + 1 and len(word)."""
        
        v = ''
        count = 0
        for i in range(pos+1, len(word)):
            if is_vowel(word[i]):
                v += word[i]
                count++
        if count == 0:
            return ''
        
        # If there are more than one vowels between pos and len(word), return the closest one. Others could be returned in the reverse order of their positions.
        elif count > 1:
            for j in range(count-2, -1, -1):
                if is_vowel(word[j]):
                    v += word[j].lower()
    
        
        
    return get_closest_vowel("full") # Get Vowel "U" and all other vowels in the Reverse order of their positions. 
