    if strings.Count(file_name, ".") != 1 {
        return "No"
    }
    if len(file_name) <= 3 {
        return "No"
    }
    if file_name[0] < 'a' || file_name[0] > 'z' && file_name[0] < 'A' || file_name[0] > 'Z' {
        return "No"
    }
    if strings.HasSuffix(file_name, ".txt") || strings.HasSuffix(file_name, ".dll") || strings.HasSuffix(file_name, ".exe") {
        return "Yes"
    }
    return "No"
}




In this problem, we need to check a file name is valid or not. A file name is considered valid if it meets all of the following requirements:

- It contains at most 3 digits.
- It contains exactly one dot.
- The substring before the dot is not empty and starts with a letter from the Latin alphabet.
- The substring after the dot is one of the following: "txt", "exe", "dll".

Here is a Python solution:

```
def check_validity(file_name):
    # Check if file name contains at most 3 digits
    if file_name.count('0') + file_name.count('1') + file_name.count('2') + file_name.count('3') + file_name.count('4') + file_name.count('5') + file_name.count('6') + file_name.count('7') + file_name.count('8') + file_name.count('9') > 3:
        return False

    # Check if file name contains exactly one dot
    if file_name.count('.') != 1:
        return False

    # Check if the substring before the dot is not empty and starts with a letter from the Latin alphabet
    if file_name[file_name.find('.')+1:].isalpha() == False or file_name[:file_name.find('.')] == '':
        return False

    # Check if the