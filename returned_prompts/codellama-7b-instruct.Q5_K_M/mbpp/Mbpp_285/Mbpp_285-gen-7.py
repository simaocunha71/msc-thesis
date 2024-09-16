```
def text_match_two_three(my_string):
    return my_string.startswith('a') and len(my_string) - my_string.index('a') in [2,3]
```
