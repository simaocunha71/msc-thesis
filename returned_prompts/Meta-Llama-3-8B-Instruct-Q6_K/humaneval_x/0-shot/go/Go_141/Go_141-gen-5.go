Here is a Go solution for the problem:

```go
package main

import (
    "strings"
    "regexp"
)

func FileNameCheck(file_name string) string {
    if !strings.Contains(file_name, ".") {
        return "No"
    }
    parts := strings.Split(file_name, ".")
    if len(parts) != 2 {
        return "No"
    }
    if !regexp.MustCompile(`^[a-zA-Z]+$`).MatchString(parts[0]) {
        return "No"
    }
    if !regexp.MustCompile(`^(txt|exe|dll)$`).MatchString(parts[1]) {
        return "No"
    }
    if len(regexp.MustCompile(`\d`).FindAllString(file_name, -1)) > 3 {
        return "No"
    }
    return "Yes"
}

func main() {
    fmt.Println(FileNameCheck("example.txt"))  // Yes
    fmt.Println(FileNameCheck("1example.dll")) // No
}
```

The function `FileNameCheck` takes a file name as input and checks whether it is valid according to the conditions specified in the problem. It checks if the file name contains a dot, if the dot is followed by exactly one extension, if the extension is one of the allowed types, and if the file name does not contain more than three digits. If all these conditions are met, it returns "Yes", otherwise it returns "No". The `main` function is used to test the `FileNameCheck` function. It prints the result of `FileNameCheck` for the file names "example.txt" and "1example.dll". The expected results are "Yes" and "No", respectively.