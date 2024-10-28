Here is a Go solution for the problem:

```go
package main

import (
    "fmt"
    "regexp"
    "strings"
)

func FileNameCheck(file_name string) string {
    if strings.Count(file_name, ".") != 1 {
        return "No"
    }
    parts := strings.Split(file_name, ".")
    if len(parts[0]) == 0 || !regexp.MustCompile(`^[a-zA-Z][a-zA-Z0-9]*$`).MatchString(parts[0]) {
        return "No"
    }
    if len(parts[1]) > 3 {
        return "No"
    }
    extensions := []string{"txt", "exe", "dll"}
    if !regexp.MustCompile(`^(txt|exe|dll)$`).MatchString(parts[1]) {
        return "No"
    }
    return "Yes"
}

func main() {
    fmt.Println(FileNameCheck("example.txt"))  // Yes
    fmt.Println(FileNameCheck("1example.dll")) // No
}
```

The function `FileNameCheck` checks the given file name against the specified conditions. It splits the file name into two parts using the dot as a separator. The first part is checked to ensure it starts with a letter from the latin alphabet and does not contain more than one digit. The second part is checked to ensure it is one of the allowed extensions. If all conditions are met, the function returns "Yes", otherwise it returns "No". The `regexp` package is used to simplify the pattern matching. The `main` function demonstrates the usage of the `FileNameCheck` function.