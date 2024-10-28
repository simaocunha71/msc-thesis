    if strings.Count(file_name, ".") != 1  {
        return "No"
    }

    parts := strings.Split(file_name, ".")
    if !((len(parts[0]) > 0) && (parts[0][0] >= 'a' && parts[0][0] <= 'z' || parts[0][0] >= 'A' && parts[0][0] <= 'Z')) {
        return "No"
    }

    if strings.ContainsAny(parts[0], "0123456789") {
        counter := 0
        for _, c := range parts[0] {
            if c >= '0' && c <= '9' {
                counter += 1
            }
        }
        if counter > 3 {
            return "No"
        }
    }

    if parts[1] != "txt" && parts[1] != "exe" && parts[1] != "dll" {
        return "No"
    }

    return "Yes"
}


A: The following code is written in Go programming language. It checks if a file's name is valid. A file's name is considered to be valid if and only if all the following conditions are met:

- There should not be more than three digits ('0'-'9') in the file's name.
- The file's name contains exactly one dot '.'
- The substring before the dot should not be empty, and it starts with a letter from the latin alphapet ('a'-'z' and 'A'-'Z').
- The substring after the dot should be one of these: ['txt', 'exe', 'dll']

The function FileNameCheck takes a string representing a file's name as input and returns a string 'Yes' if the file's name is valid, and 'No' otherwise.

The function uses the strings.Count function to count the number of dots in the file name. If there is not exactly one dot, the function returns 'No'.

The function then splits the file name into two parts using the strings.Split function. The function checks if the first part of the file name is not empty