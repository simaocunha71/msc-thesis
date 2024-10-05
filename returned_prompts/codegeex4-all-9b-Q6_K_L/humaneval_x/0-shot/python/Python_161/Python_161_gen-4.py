def solve(s):
    result = ""
    letter_count = 0
    for char in s:
        if char.isalpha():
            letter_count += 1
            if char.isupper():
                result += char.lower()
            else:
                result += char.upper()
        else:
            result += char
    if letter_count == 0:
        result = result[::-1]
    return result

print(solve("1234"))  # "4321"
print(solve("ab"))  # "AB"
print(solve("#a@C"))  # "#A@c"