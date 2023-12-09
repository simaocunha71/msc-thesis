
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
        return c.lower() in set('aeiou')

    def remove_consonants(str, l=10, r=-1):
        while (l >= 0) and (r < len(str)):
            if not is_vowel(str[r]) or str[r] == 'y':
                return str[:l + r + 2], remove_consonants(str, l - 1, r)
            else:
                return str, ''
        return '', ''

    def vowel_count(str):
        count = sum([1 if is_vowel(c) else 0 for c in str])
        return count % len(set('aeiou'))

    def closest_vowel(word, i=len(word)-1, j=-1, k=0):
        vowels = set()
        if i >= -1:
            vowels.add(word[i])

        if j != -1 and i != 0:
            vowels += set([y[j-1] for y in remove_consonants(word, j - 1, i + j)])

        word = list(remove_consonants(word, k))
        if len(set(list(word))) == len(vowels):
            return ''.join(['%s' % w for w in vowels]), closest_vowel