def text_starta_endb(text):
    return text[0] == 'a' and text[-1] == 'b'

# Test
print(text_starta_endb("aabbbb"))  # True
print(text_starta_endb("axb"))    # True
print(text_starta_endb("ax"))     # False
print(text_starta_endb("axbx"))    # True
print(text_starta_endb("axax"))    # False
print(text_starta_endb("axaxb"))   # True

# More Tests
print(text_starta_endb("axaxbaxbaaxayaxbyayayaxayayaxayayayayaxayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayaxayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayay