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
    if strings.Count(file_name, ".") > 1 {
        return "No"
    }
    if strings.Count(file_name, ".") == 0 {
        return "No"
    }
    if len(file_name) > 3 {
        return "No"
    }
    if file_name[0] < 65 || file_name[0] > 90 {
        return "No"
    }
    if file_name[len(file_name)-1] != "txt" && file_name[len(file_name)-1] != "exe" && file_name[len(file_name)-1] != "dll" {
        return "No"
    }
    return "Yes"
}
