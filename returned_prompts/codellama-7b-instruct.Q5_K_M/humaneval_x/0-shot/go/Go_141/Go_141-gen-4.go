import (
    "fmt"
    "regexp"
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
    r, _ := regexp.Compile("^([a-zA-Z]+)\\.([txt|exe|dll])$")
    if !r.MatchString(file_name) {
        return "No"
    }
    return "Yes"
}

func main() {
    fmt.Println(FileNameCheck("example.txt"))
    fmt.Println(FileNameCheck("1example.dll"))
    fmt.Println(FileNameCheck("example.exe"))
    fmt.Println(FileNameCheck("example.dll"))
    fmt.Println(FileNameCheck("example.doc"))
    fmt.Println(FileNameCheck("example.exe.exe"))
    fmt.Println(FileNameCheck("example.txt.exe"))
    fmt.Println(FileNameCheck("example.exe.dll"))
    fmt.Println(FileNameCheck("example.txt.dll"))
}

