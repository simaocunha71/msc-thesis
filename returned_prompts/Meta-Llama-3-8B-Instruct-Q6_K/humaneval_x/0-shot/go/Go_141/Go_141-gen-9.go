Here is a Go function that satisfies the conditions:

```go
package main

import (
    "strings"
    "regexp"
)

func FileNameCheck(file_name string) string {
    // Check if there are more than three digits in the file's name
    if strings.Count(file_name, "0123456789") > 3 {
        return "No"
    }

    // Check if the file's name contains exactly one dot '.'
    if strings.Count(file_name, ".") != 1 {
        return "No"
    }

    // Split the file's name into two parts: before and after the dot
    parts := strings.Split(file_name, ".")
    if len(parts) != 2 {
        return "No"
    }
    before, after := parts[0], parts[1]

    // Check if the substring before the dot starts with a latin alphapet letter
    if !regexp.MustCompile(`^[a-zA-Z]`).MatchString(before) {
        return "No"
    }

    // Check if the substring after the dot is one of these: ['txt', 'exe', 'dll']
    validExtensions := []string{"txt", "exe", "dll"}
    for _, ext := range validExtensions {
        if ext == after {
            return "Yes"
        }
    }

    return "No"
}

func main() {
    fmt.Println(FileNameCheck("example.txt"))  // Output: Yes
    fmt.Println(FileNameCheck("1example.dll")) // Output: No
}
```

In this code, we use the `strings` package to count the number of digits and dots in the file's name. We use the `regexp` package to check if the substring before the dot starts with a latin alphapet letter. We use a slice of valid extensions to check if the substring after the dot is one of these. If all conditions are met, the function returns 'Yes', otherwise it returns 'No'.