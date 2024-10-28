def get_closest_vowel(word):
    for i in range(len(word)-2, -1, -1):
        if word[i].lower() in 'aeiou':
            return word[i]
    return ""


# Test cases
print(get_closest_vowel("yogurt"))  # Expected output: "u"
print(get_closest_vowel("FULL"))  # Expected output: "U"
print(get_closest_vowel("quick"))  # Expected output: ""
print(get_closest_vowel("ab"))  # Expected output: ""
print(get_closest_vowel("banana"))  # Expected output: "a" 
print(get_closest_vowel("hello"))  # Expected output: "e" 
print(get_closest_vowel("cde"))  # Expected output: "e" 
print(get_closest_vowel("aeiou"))  # Expected output: "" 
print(get_closest_vowel("bcdfghjklmnpqrstvwxyz"))  # Expected output: ""
print(get_closest_vowel("z"))  # Expected output: "" 
print(get_closest_vowel("xyz"))  # Expected output: "" 
print(get_closest_vowel("xy"))  # Expected output: "" 
print(get_closest_vowel("x"))  # Expected output: "" 
print(get_closest_vowel("y"))  # Expected output: ""  # Expected output: "" 
print(get_closest_vowel("bcdfghjklmnpqrstvwxyz"))  # Expected output: ""
print(get_closest_vowel("bcdfghjklmnpqrstvwxyz"))  # Expected output: ""
print(get_closest_vowel("bcdfghjklmnpqrstvwxyz"))  # Expected output: ""
print(get_closest_vowel("bcdfghjklmnpqrstvwxyz"))  # Expected output: ""
print(get_closest_vowel("bcdfghjklmnpqrstvwxyz"))  # Expected output: ""
print(get_closest_vowel("bcdfghjklmnpqrstvwxyz"))  # Expected output: ""
print(get_closest_vowel("bcdfghjklmnpqrstvwxyz"))  # Expected output: ""
print(get_closest_vowel("bcdfghjklmnpqrstvwxyz"))  # Expected output: ""
print(get_closest_vowel("bcdfghjklmnpqrstvwxyz"))  # Expected output: