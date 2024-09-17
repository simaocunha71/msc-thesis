```
import re

def check_str(s):
    if re.match('^[aeiouAEIOU]', s):
        return True
    else:
        return False
```
The function check_str() takes a string s as input and checks if it starts with a vowel (both lowercase and uppercase) using regular expression. The pattern '^[aeiouAEIOU]' matches any string that starts with a vowel. If the string matches this pattern, it returns True; otherwise, it returns False. 

The unit test `assert check_str("annie")` ensures that the function correctly identifies strings that start with vowels. In this case, "annie" starts with the vowel "a", so the function should return True. 

Note: The unit test is not provided in the original problem statement, but it's included here to demonstrate how the function can be tested. The function can also be tested with other strings that start with vowels or consonants to ensure its correctness. 