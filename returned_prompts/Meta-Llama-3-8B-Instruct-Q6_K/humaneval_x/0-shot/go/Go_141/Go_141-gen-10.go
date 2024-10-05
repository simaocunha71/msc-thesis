Here is a Go solution for the problem:

```go
package main

import (
    "strings"
    "regexp"
)

func FileNameCheck(file_name string) string {
    // Check if the file name contains more than three digits
    if strings.Count(file_name, "0") > 3 || strings.Count(file_name, "1") > 3 || strings.Count(file_name, "2") > 3 || strings.Count(file_name, "3") > 3 || strings.Count(file_name, "4") > 3 || strings.Count(file_name, "5") > 3 || strings.Count(file_name, "6") > 3 || strings.Count(file_name, "7") > 3 || strings.Count(file_name, "8") > 3 || strings.Count(file_name, "9") > 3 {
        return "No"
    }

    // Check if the file name contains exactly one dot
    if strings.Count(file_name, ".") != 1 {
        return "No"
    }

    // Split the file name into two parts: the part before the dot, and the part after the dot
    parts := strings.Split(file_name, ".")

    // Check if the part before the dot starts with a latin alphapet letter
    if !regexp.MustCompile(`^[a-zA-Z]`).MatchString(parts[0]) {
        return "No"
    }

    // Check if the part after the dot is one of these: ['txt', 'exe', 'dll']
    extensions := []string{"txt", "exe", "dll"}
    if !regexp.MustCompile(`^(txt|exe|dll)$`).MatchString(parts[1]) {
        if !regexp.MustCompile(`^(txt|exe|dll)$`).MatchString(strings.ToLower(parts[1])) {
            return "No"
        }
    }

    return "Yes"
}

func main() {
    fmt.Println(FileNameCheck("example.txt"))  // Output: Yes
    fmt.Println(FileNameCheck("1example.dll")) // Output: No
}
```

This code first checks if the file name contains more than three digits. Then it splits the file name into two parts: the part before the dot, and the part after the dot. It checks if the part before the dot starts with a latin alphapet letter and if the part after the dot is one of these: ['txt', 'exe', 'dll']. The function returns 'Yes' if all conditions are met, and 'No' otherwise