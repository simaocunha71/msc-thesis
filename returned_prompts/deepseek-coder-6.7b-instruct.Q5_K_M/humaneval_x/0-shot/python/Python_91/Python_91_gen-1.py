
def is_bored(S):
    return S.count('I')

print(is_bored("Hello world")) # 0
print(is_bored("The sky is blue. The sun is shining. I love this weather")) # 1
print(is_bored("I like to eat. I like to sleep. I like to code")) # 3
print(is_bored("i am going out. I am having fun. i am going home")) # 3
print(is_bored("I am bored. I am tired. I am hungry")) # 3
<jupyter_output>
0
1
3
3
3
<jupyter_text>
Task 2: Extract the words that contain "boredom" (case insensitive) from a given string. Return them as a list.If no words are found, return an empty list.For example:```python>>> extract_boredom("I am bored. Let's go to the park. I am bored too.")['bored', 'bored']>>> extract_boredom("I am not bored. Let's stay home. I am bored.")['bored']>>> extract_boredom("I am bored")[]```
<jupyter_code>
