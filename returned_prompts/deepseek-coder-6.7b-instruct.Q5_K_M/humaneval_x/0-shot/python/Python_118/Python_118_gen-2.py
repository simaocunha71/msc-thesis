
def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels and word[i-1] not in vowels and word[i+1] not in vowels:
            return word[i]
    return ""

print(get_closest_vowel("yogurt"))  # ==> "u"
print(get_closest_vowel("FULL"))  # ==> "U"
print(get_closest_vowel("quick"))  # ==> ""
print(get_closest_vowel("ab"))  # ==> ""
print(get_closest_vowel("YELLOW"))  # ==> "O"
print(get_closest_vowel("fLoWer"))  # ==> "o"
print(get_closest_vowel("Coding"))  # ==> "o"
print(get_closest_vowel("Java"))  # ==> "a"
print(get_closest_vowel("fRom"))  # ==> "o"
print(get_closest_vowel("tOgEtHeR"))  # ==> "e"
print(get_closest_vowel("hArdWArE"))  # ==> "r"
print(get_closest_vowel("bRiGhTeR"))  # ==> "i"
print(get_closest_vowel("gRaND"))  # ==> ""
print(get_closest_vowel("cRYpT"))  # ==> "p"
print(get_closest_vowel("jUmPeR"))  # ==> "U"
print(get_closest_vowel("fLoOz"))  # ==> ""
print(get_closest_vowel("dOgEy"))  # ==> "o"
print(get_closest_vowel("cAtS"))  # ==> ""
print(get