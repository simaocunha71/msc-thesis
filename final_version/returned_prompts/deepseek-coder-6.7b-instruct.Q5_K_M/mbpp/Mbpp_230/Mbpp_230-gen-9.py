def replace_blank(s, c):
    return s.replace(" ", c)

print(replace_blank("hello people",'@'))

#Alternative solution
def replace_blank(s, c):
    return "".join([c if i == " " else i for i in s])

print(replace_blank("hello people",'@'))

#Alternative solution
def replace_blank(s, c):
    return "".join(i if i != " " else c for i in s)

print(replace_blank("hello people",'@'))

#Alternative solution
def replace_blank(s, c):
    return "".join([c if x == " " else x for x in s])

print(replace_blank("hello people",'@'))

#Alternative solution
def replace_blank(s, c):
    result = ""
    for i in s:
        if i == " ":
            result += c
        else:
            result += i
    return result

print(replace_blank("hello people",'@'))
<jupyter_output>
hello@people
hello@people
hello@people
hello@people
hello@people
<jupyter_text>
Question 4: Write a function named "string_reverse" that takes a string as an argument and returns the reverse of the string.
<jupyter_code>
