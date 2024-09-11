"""
def text_match_wordz_middle(string):
    #check if the string contains 'z'
    if 'z' not in string:
        return False
    #check if the first and last character are 'z'
    if string[0] == 'z' or string[-1] == 'z':
        return False
    #if none of the above conditions are met, return true
    return True
"""

def text_match_wordz_middle(string):
    #check if the string contains 'z'
    if 'z' not in string:
        return False
    #check if the first and last character are 'z'
    if string[0] == 'z' or string[-1] == 'z':
        return False
    #if none of the above conditions are met, return true
    return True

#test
print(text_match_wordz_middle("pythonzabc.")) #True
#print(text_match_wordz_middle("pythonz")) #False
#print(text_match_wordz_middle("abcz")) #False
#print(text_match_wordz_middle("z")) #False
#print(text_match_wordz_middle("zc")) #False
#print(text_match_wordz_middle("cza")) #False
#print(text_match_wordz_middle("cz")) #False
#print(text_match_wordz_middle("a.z")) #False
#print(text_match_wordz_middle("abcz.")) #True
#print(text_match_wordz_middle("abcz")) #True
#print(text_match_wordz_middle("abcza")) #False
#print(text_match_wordz_middle("abc.z")) #True
#print(text_match_wordz_middle("abcz.")) #True
#print(text_match_wordz_middle("abcz")) #True
#print(text_match_wordz_middle("abcza")) #False
#print(text_match_wordz_middle("abc.z")) #True
#print(text_match_wordz_middle("abcz")) #True
#print(text_