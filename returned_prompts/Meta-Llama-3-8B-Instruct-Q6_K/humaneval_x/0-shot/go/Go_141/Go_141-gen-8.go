Here is the solution in Go:
```go
package main

import (
    "fmt"
    "regexp"
    "strings"
)

func FileNameCheck(file_name string) string {
    // Check if the file name contains more than three digits
    if len(regexp.MustCompile(`\d{4,}`).FindAllString(file_name, -1)) > 0 {
        return "No"
    }

    // Check if the file name contains exactly one dot
    if strings.Count(file_name, ".") != 1 {
        return "No"
    }

    // Split the file name into two parts: before the dot and after the dot
    parts := strings.Split(file_name, ".")

    // Check if the substring before the dot starts with a letter from the latin alphapet
    if !regexp.MustCompile(`^[a-zA-Z]`).MatchString(parts[0]) {
        return "No"
    }

    // Check if the substring after the dot is one of these: ['txt', 'exe', 'dll']
    if !(regexp.MustCompile(`^(txt|exe|dll)$`).MatchString(parts[1])) {
        return "No"
    }

    return "Yes"
}

func main() {
    fmt.Println(FileNameCheck("example.txt"))  // Output: Yes
    fmt.Println(FileNameCheck("1example.dll")) // Output: No
}
```
In this solution, we use regular expressions to check the file name for the specified conditions. The `regexp.MustCompile` function is used to compile the regular expression pattern, and the `MatchString` method is used to check if the pattern matches a given string. The `strings.Split` function is used to split the file name into two parts: before the dot and after the dot. The `strings.Count` function is used to count the number of dots in the file name. The `fmt.Println` function is used to print the result of the `FileNameCheck` function.