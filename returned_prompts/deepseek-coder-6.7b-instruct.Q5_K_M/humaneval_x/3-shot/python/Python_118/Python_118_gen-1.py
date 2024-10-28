
def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word  (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """

    vowels = 'aeiouAEIOU'
    word = word[::-1]
    for i in range(1, len(word) - 1):
        if word[i] in vowels and word[i - 1] not in vowels and word[i + 1] not in vowels:
            return word[i]
    return ''

print(get_closest_vowel("yogurt"))  #==> "u"
print(get_closest_vowel("FULL"))  #==> "U"
print(get_closest_vowel("quick"))  #==> ""
print(get_closest_vowel("ab"))  #==> ""

# The function works by reversing the input word and then iterating over it. For each character, it checks if it is a vowel and if the characters on its left and right are not vowels. If it is, it returns the character. If no such character is found after checking all characters