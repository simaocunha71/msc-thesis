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
    if len(strings.Split(file_name, ".")[0]) > 3 { return "No" } // file_name contains more than three digits and it's invalid
    
    if !strings.HasPrefix(strings.TrimSpace(strings.Split(file_name, ".")[0]), "a") && !strings.HasPrefix(strings.TrimSpace(strings.Split(file_name, ".")[0]), "A") { return "No" } // file's name starts with a non-alpha char and it's invalid
    if strings.HasSuffix(strings.TrimSpace(strings.Split(file_name, ".")[1:]), "txt") || strings.HasSuffix(strings.TrimSpace(strings.Split(file_name, ".")[1:]), "EXE") || strings.HasSuffix(strings.TrimSpace(strings.Split(file_name, ".")[1:]), "DLL") { return "Yes" } // file's name ends with a valid string
    
    return "No"
}