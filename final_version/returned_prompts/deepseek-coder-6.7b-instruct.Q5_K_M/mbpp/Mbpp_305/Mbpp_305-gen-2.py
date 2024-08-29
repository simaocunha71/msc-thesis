
def start_withp(words):
    result = []
    for word in words:
        split_word = word.split()
        for sw in split_word:
            if sw.lower().startswith('p'):
                result.append(sw)
    return tuple(result)

print(start_withp(["Python PHP", "Java JavaScript", "c c++"]))

#Output: ('Python', 'PHP')


#Alternative solution
def start_withp(words):
    return tuple(word for word in words.split() if word.lower().startswith('p'))

print(start_withp("Python PHP Java JavaScript c c++"))

#Output: ('Python', 'PHP')
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3
<jupyter_code>
