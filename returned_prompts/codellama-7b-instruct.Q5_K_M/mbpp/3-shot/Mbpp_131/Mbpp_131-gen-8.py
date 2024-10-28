
def reverse_vowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        if char in vowels:
            result = char + result
        else:
            result = result + char
    return result


