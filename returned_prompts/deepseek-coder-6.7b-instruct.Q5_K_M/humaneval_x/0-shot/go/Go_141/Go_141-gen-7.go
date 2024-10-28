    if len(file_name) > 256 {
        return "No"
    }

B:
    count := strings.Count(file_name, ".")
    if count != 1 {
        return "No"
    }

C:
    parts := strings.Split(file_name, ".")
    if len(parts[0]) == 0 || !(parts[0][0] >= 'a' && parts[0][0] <= 'z' || parts[0][0] >= 'A' && parts[0][0] <= 'Z') {
        return "No"
    }

D:
    if !strings.Contains(file_name, ".txt") && !strings.Contains(file_name, ".exe") && !strings.Contains(file_name, ".dll") {
        return "No"
    }

E:
    if strings.Count(file_name, "")-1 > 3 {
        return "No"
    }

F:
    return "Yes"

}


A: The function should check if the file name is not too long (maximum 256 characters).
B: The function should check if there is exactly one dot in the file name.
C: The function should check if the part before the dot starts with a latin alphapet letter.
D: The function should check if the part after the dot is one of these:  ['txt',  'exe',  'dll'].
E: The function should check if there are not more than three digits in the file name.
F: If all the conditions are met, the function should return 'Yes'.

A: The function should return 'No' if the file name is too long (more than 256 characters).
B: The function should return 'No' if there are more than one dot in the file name.
C: The function should return 'No' if the part before the dot does not start with a latin alphapet letter.
D: The function should return 'No' if the part after the dot is not one of these:  ['txt',  'exe',  'dll'].
E: The function should return 'No' if there are more than three digits