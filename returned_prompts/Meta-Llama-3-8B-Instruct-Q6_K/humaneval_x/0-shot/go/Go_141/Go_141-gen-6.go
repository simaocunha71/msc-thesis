```go
package main

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
func FileNameCheck(file_name string) string {
    parts := strings.Split(file_name, ".")
    if len(parts) != 2 {
        return "No"
    }
    if !strings.HasPrefix(parts[0], strings.ToUpper(strings.ToLower(parts[0]))[0:1]) {
        return "No"
    }
    if len(strings.Replace(parts[0], strings.ToLower(parts[0]), "", -1)) > 0 {
        return "No"
    }
    if len(strings.Replace(parts[1], "txt", "", -1)) > 0 && len(strings.Replace(parts[1], "exe", "", -1)) > 0 && len(strings.Replace(parts[1], "dll", "", -1)) > 0 {
        return "No"
    }
    for _, c := range parts[0] {
        if c >= '0' && c <= '9' {
            if strings.Count(string(c), string(c)) > 3 {
                return "No"
            }
        }
    }
    if strings.Count(parts[1], ".") > 0 {
        return "No"
    }
    return "Yes"
}

func main() {
    fmt.Println(FileNameCheck("example.txt"))  // => 'Yes'
    fmt.Println(FileNameCheck("1example.dll")) // => 'No'
}
```


Here is the explanation of the code:
- The function splits the file name into two parts at the dot.
- It checks if the file name contains exactly one dot.
- It checks if the first part of the file name starts with a letter from the latin alphabet.
- It checks if the first part of the file name does not contain digits more