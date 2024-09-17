import re
import re
import re
def start_withp(words):
    lst = []
    for i in words:
        if i[0]=='p':
            lst.append(i)
    return (lst[0], lst[1])