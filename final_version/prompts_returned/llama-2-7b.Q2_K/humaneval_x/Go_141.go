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
    if len(strings.TrimSpace(file_name)) == 0 {
        return "No" // file doesn't have any name
    }
    valid := true
    is_empty_before_dot := strings.HasPrefix(file_name, ".") && strings.Count(file_name, ".") <= 1
    if len(strings.TrimSpace(file_name[strings.IndexRune(file_name, '.'):])) == 0 {
        valid = false // file name is empty before the dot
    } else {
        for _, r := range strings.Split(file_name[:strings.IndexRune(file_name, '.')], ".") {
            if !isdigit(r) && !isalpha(r) && !isspace(r) && r != '.' {
                valid = false // the substring is not valid
                break
            }
        }
    }
    if len(strings.TrimSpace(file_name[strings.IndexRune(file_name, '.')+1:])) == 0 {
        return "No" // file doesn't have extension after the dot
    }
    valid = false // the