Here is a Go function that implements the FileNameCheck function as described:

```go
package main

import (
    "strings"
    "regexp"
)

func FileNameCheck(file_name string) string {
    // Check if the file's name contains more than three digits
    if strings.Count(file_name, "0123456789") > 3 {
        return "No"
    }

    // Check if the file's name contains exactly one dot
    parts := strings.Split(file_name, ".")
    if len(parts) != 2 {
        return "No"
    }

    // Check if the substring before the dot starts with a latin alphapet letter
    if !regexp.MustCompile(`^[a-zA-Z]`).MatchString(parts[0]) {
        return "No"
    }

    // Check if the substring after the dot is one of the allowed extensions
    allowedExtensions := []string{"txt", "exe", "dll"}
    if !regexp.MustCompile(strings.Join(allowedExtensions, "|")).MatchString(parts[1]) {
        return "No"
    }

    return "Yes"
}
```

This function first checks if the file's name contains more than three digits. If it does, it returns "No". Then it checks if the file's name contains exactly one dot. If it doesn't, it returns "No". Then it checks if the substring before the dot starts with a latin alphapet letter. If it doesn't, it returns "No". Finally, it checks if the substring after the dot is one of the allowed extensions. If it's not, it returns "No". If all checks pass, it returns "Yes". The function uses the `strings` and `regexp` packages to perform the checks. The `regexp` package is used to match the allowed extensions. The `regexp.MustCompile` function is used to compile a regular expression, and the `MatchString` method is used to match a string against the regular expression. The `strings` package is used to split the file's name into parts, and to count the number of digits in the file's name. The `regexp` package is used to match the allowed extensions. The `regexp.MustCompile` function is used to compile a regular expression, and the `MatchString` method is used to match a string against the regular expression. The `strings` package is used to split the file's name into parts, and to count the number of digits in the file's name. The `regexp` package is used to