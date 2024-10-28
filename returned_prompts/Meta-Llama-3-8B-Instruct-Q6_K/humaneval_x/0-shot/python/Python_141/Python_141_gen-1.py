```
def file_name_check(file_name):
    if not isinstance(file_name, str):
        return 'No'
    if not file_name:
        return 'No'
    if len(file_name.split('.')) != 2:
        return 'No'
    before_dot, after_dot = file_name.rsplit('.', 1)
    if not before_dot[0].isalpha():
        return 'No'
    if before_dot.count('0') + before_dot.count('1') + before_dot.count('2') + before_dot.count('3') + before_dot.count('4') + before_dot.count('5') + before_dot.count('6') + before_dot.count('7') + before_dot.count('8') + before_dot.count('9') > 3:
        return 'No'
    if after_dot.lower() not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
```





Explanation:
The function takes a string representing a file's name as input. It first checks if the input is not a string, in which case it returns 'No'. Then it checks if the file name is empty, in which case it also returns 'No'. It then splits the file name into two parts at the dot and checks if there are exactly two parts. If not, it returns 'No'. It then checks if the first character of the part before the dot is a letter from the latin alphabet. If not, it returns 'No'. It also checks if there are more than three digits in the part before the dot. If there are, it returns 'No'. Finally, it checks if the part after the dot is one of the allowed extensions ('txt', 'exe', 'dll'). If not, it returns 'No'. If all these conditions are met, it returns 'Yes'.