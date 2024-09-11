def text_lowercase_underscore(input_string):
    underscore_list = input_string.split("_")
    for i in range(len(underscore_list)):
        if underscore_list[i] != underscore_list[i].lower():
            return False
    return True

#print(text_lowercase_underscore("aab_cbbbc"))
#print(text_lowercase_underscore("aab_cbbbc_dde"))
#print(text_lowercase_underscore("aAb_cBBbc"))
#print(text_lowercase_underscore("aab_cbbbc_dde_ee"))
#print(text_lowercase_underscore("aabcdc"))
#print(text_lowercase_underscore("aabcdc_"))
#print(text_lowercase_underscore("aabcdc_bcd"))

def text_lowercase_underscore(input_string):
    underscore_list = input_string.split("_")
    for i in range(len(underscore_list)):
        if underscore_list[i] != underscore_list[i].lower():
            return False
    return True

#print(text_lowercase_underscore("aab_cbbbc"))
#print(text_lowercase_underscore("aab_cbbbc_dde"))
#print(text_lowercase_underscore("aab_cbbbc_dde_ee"))
#print(text_lowercase_underscore("aabcdc"))
#print(text_lowercase_underscore("aabcdc_"))
#print(text_lowercase_underscore("aabcdc_bcd"))

text_lowercase_underscore("aab_cbbbc")
text_lowercase_underscore("aab_cbbbc_dde")
text_lowercase_underscore("aabcdc")
text_lowercase_underscore("aabcdc_")
text_lowercase_underscore("aabcdc_bcd")

"""
The