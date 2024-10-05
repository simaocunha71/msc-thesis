import (
    "strings"
)

// Create a function which takes a string representing a file's name, and returns
// 'Yes' if the the file's name is valid, and returns 'No' otherwise.
// A file's name is considered to be valid if and only if all the following conditions
// are met:
// - There should not be more than three digits ('0'-'9') in the file's name.
// - The file's name contains exactly one dot '.'
// - The substring before the dot should not be empty, and it starts with a letter from
// the latin alphapet ('a'-'z' and 'A'-'Z').
// - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
// Examples:
// FileNameCheck("example.txt") # => 'Yes'
// FileNameCheck("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
func FileNameCheck(file_name string) string {

    if len(file_name) > 8 {
        return "No"
    }

    if strings.Count(file_name, ".") != 1 {
        return "No"
    }

    if len(file_name) < 4 {
        return "No"
    }

    if file_name[0] >= 'a' && file_name[0] <= 'z' || file_name[0] >= 'A' && file_name[0] <= 'Z' {
        return "Yes"
    }

    for _, v := range file_name {
        if v >= '0' && v <= '9' {
            return "No"
        }
    }

    return "Yes"

}