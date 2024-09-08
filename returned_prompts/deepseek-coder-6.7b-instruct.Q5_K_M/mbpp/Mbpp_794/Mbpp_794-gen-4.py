def text_starta_endb(txt):
    if re.fullmatch(r'a.*b$', txt):
        return True
    else:
        return False

# test cases
print(text_starta_endb("aabbbb")) # True
print(text_starta_endb("ababab")) # False
print(text_starta_endb("aabbb"))  # False
print(text_starta_endb("a"))     # False
print(text_starta_endb("ab"))    # True

