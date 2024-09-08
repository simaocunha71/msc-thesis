
def text_start1_end2(text):
    if re.search(r'1.*2$', text):
        return True
    else:
        return False

print(text_start1_end2("1anything2"))
print(text_start1_end2("1anything3"))

#Q5:
"""
Write a function that matches a string that has a '