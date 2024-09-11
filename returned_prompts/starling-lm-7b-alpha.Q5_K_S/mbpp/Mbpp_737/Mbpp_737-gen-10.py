"""
def check_str(string):
    vowels = "[aeiou]"
    if re.match(vowels, string[0]):
        return True
    else:
        return False
"""

def check_str(string):
    vowels = "[aeiou]"
    if re.match(vowels, string[0]):
        return True
    else:
        return False


#assert check_str("annie")
#assert not check_str("bob")
#assert check_str("dave")
#assert not check_str("elizabeth")
#assert check_str("frank")
#assert check_str("gertrude")
#assert not check_str("harold")
#assert not check_str("isabel")
#assert check_str("james")
#assert check_str("karen")
#assert not check_str("louise")
#assert check_str("mark")
#assert check_str("nina")
#assert check_str("olga")
#assert not check_str("peter")
#assert not check_str("queen")
#assert check_str("robert")
#assert check_str("samantha")
#assert check_str("tina")
#assert check_str("umar")
#assert not check_str("vicky")
#assert check_str("walter")
#assert check_str("xavier")
#assert check_str("yolanda")
#assert check_str("zoe")


print(check_str("annie"))
print(check_str("bob"))
print(check_str("dave"))
print(check_str("elizabeth"))
print(check_str("frank"))
print(check_str("gertrude"))
print(check_str("harold"))
print(check_str("isabel"))
print(check_str("james"))
print(check_str("karen"))
print(check_str("louise"))
print(check_str("mark"))
print(check_str("nina"))
print(check_str("olga"))
print(check