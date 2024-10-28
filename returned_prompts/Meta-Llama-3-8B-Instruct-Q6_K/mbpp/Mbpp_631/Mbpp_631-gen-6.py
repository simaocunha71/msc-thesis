def replace_spaces(s):
    result = ""
    for char in s:
        if char == " ":
            result += "_"
        elif char == "_":
            result += " "
        else:
            result += char
    return result
# test
print(replace_spaces('Jumanji The Jungle'))  # Expected output: Jumanji_The_Jungle
print(replace_spaces('Jumanji_The_Jungle'))  # Expected output: Jumanji The Jungle
print(replace_spaces('   Hello   '))  # Expected output: _Hello_ 
print(replace_spaces('_Hello_'))  # Expected output:   Hello   '
print(replace_spaces('Hello'))  # Expected output: Hello
print(replace_spaces('_'))  # Expected output: 
print(replace_spaces(' '))  # Expected output: _ 
print(replace_spaces('Jumanji____Jungle'))  # Expected output: Jumanji_____Jungle
print(replace_spaces('_Jumanji____Jungle'))  # Expected output:  Jumanji____Jungle 
print(replace_spaces('_Jumanji____'))  # Expected output:   Jumanji____ 
print(replace_spaces('____Jumanji'))  # Expected output:   Jumanji 
print(replace_spaces('_____Jumanji'))  # Expected output:    Jumanji 
print(replace_spaces('_Jumanji____Jungle____'))  # Expected output:   Jumanji____Jungle____ 
print(replace_spaces('_Jumanji____Jungle____Jumanji'))  # Expected output:   Jumanji____Jungle____Jumanji 
print(replace_spaces('Jumanji____Jungle____'))  # Expected output: Jumanji____Jungle____ 
print(replace_spaces('_Jumanji____Jumanji'))  # Expected output:   Jumanji____Jumanji 
print(replace_spaces('_Jumanji____Jumanji____'))  # Expected output:   Jumanji____Jumanji____ 
print(replace_spaces('_Jumanji____Jumanji____Jumanji'))  # Expected output:   Jumanji____Jumanji____Jumanji 
print(replace_spaces('____Jumanji____Jumanji'))  # Expected output:   Jumanji____Jumanji 
print(replace_spaces('_Jumanji____Jumanji____Jumanji'))  # Expected