
def check_str(s):
    pattern = "^[aeiou]"
    if re.match(pattern, s):
        return True
    else:
        return False

print(check_str("annie"))

#output: True

"""
The function check_str takes a string as input and uses the re.match function to check if the string starts with a vowel. The pattern "^[aeiou]" is used to match the start of the string with any vowel. If the string starts with a vowel, re.match returns a match object, which is truthy. If not, it returns None, which is falsy. The function returns True if the string starts with a vowel and False otherwise.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Q2. Extract all the unique words from a given sentence.
<jupyter_code>
import re

def extract_unique_words(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    return list(set(words))

sentence = "Python is an interpreted, high-level, general-purpose programming language. Python's design philosophy emphasizes code readability with its use of significant indentation."
print(extract_unique_words(sentence))

#output: ['Python', 'high-level', 'interpreted', 'general-purpose', 'programming', 'language', 'Python\'s', 'design', 'philosophy', 'emphasizes', 'code', 'readability', 'use', 'significant', 'indentation']
<jupyter_output>
<empty_output>
<jupyter_text>
Q3. Check if the string is a valid email or not.
<jupyter_code>
import re

def check_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

print(check_email("user@domain.com"))

#output: True
<jupyter_output