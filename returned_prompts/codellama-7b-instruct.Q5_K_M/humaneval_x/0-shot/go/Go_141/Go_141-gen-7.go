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
    var (
        dotCount   int
        hasDot     bool
        isValid    bool
        isValidLen bool
        isValidStr bool
        strBefore  string
        strAfter   string
    )
    for _, char := range file_name {
        switch {
        case char >= 'a' && char <= 'z':
            isValidStr = true
        case char >= 'A' && char <= 'Z':
            isValidStr = true
        case char >= '0' && char <= '9':
            dotCount++
        case char == '.':
            hasDot = true
        default:
            isValidStr = false
        }
    }
    if isValidStr && hasDot {
        strBefore := file_name[:strings.Index(file_name, ".")]
        strAfter := file_name[strings.Index(file_name, ".")+1:]
        isValidLen = dotCount <= 3
        isValid = isValidLen && (strBefore != "" && (strBefore[0] >= 'a' && strBefore[0] <= 'z' || strBefore[0] >= 'A' && strBefore[0] <=