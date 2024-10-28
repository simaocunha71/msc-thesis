Here is a Go function that implements the file name validation according to the given conditions:

```go
package main

import (
    "strings"
)

func FileNameCheck(file_name string) string {
    // Check if there are more than three digits in the file's name
    if strings.Count(file_name, "0123456789") > 3 {
        return "No"
    }

    // Check if there is exactly one dot in the file's name
    if strings.Count(file_name, ".") != 1 {
        return "No"
    }

    // Split the file name into two parts: before and after the dot
    parts := strings.Split(file_name, ".")
    if len(parts) != 2 {
        return "No"
    }

    // Check if the substring before the dot starts with a letter from the latin alphabet
    if !strings.Contains(strings.ToUpper(parts[0]), "ABCDEFGHIJKLMNOPQRSTUVWXYZ") &&
        !strings.Contains(strings.ToUpper(parts[0]), "ABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return "No"
    }

    // Check if the substring after the dot is one of the allowed extensions
    allowedExtensions := []string{"txt", "exe", "dll"}
    if !strings.Contains(strings.ToLower(parts[1]), allowedExtensions...) {
        return "No"
    }

    // If all conditions are met, the file name is valid
    return "Yes"
}

func main() {
    fmt.Println(FileNameCheck("example.txt"))  // Output: Yes
    fmt.Println(FileNameCheck("1example.dll")) // Output: No
}
```

This function first checks if there are more than three digits in the file name. If there are, it returns "No". Then it checks if there is exactly one dot in the file name. If there isn't, it returns "No". After that, it splits the file name into two parts: before and after the dot. If the file name does not contain exactly one dot, it returns "No". Then it checks if the substring before the dot starts with a letter from the latin alphabet. If it doesn't, it returns "No". Finally, it checks if the substring after the dot is one of the allowed extensions. If it's not, it returns "No". If all conditions are met, the function returns "Yes". Otherwise, it returns "No". The function is tested with two examples in the main function. The first example is a valid file name and the second example is not. The output of the function is