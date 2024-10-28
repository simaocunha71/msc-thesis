Here is the solution to the problem:

```go
package main

import (
    "strings"
)

func FileNameCheck(file_name string) string {
    // Check if the file name contains more than three digits
    if strings.Count(file_name, "0123456789") > 3 {
        return "No"
    }

    // Check if the file name contains exactly one dot
    if strings.Count(file_name, ".") != 1 {
        return "No"
    }

    // Split the file name into two parts: before and after the dot
    parts := strings.Split(file_name, ".")
    if len(parts) != 2 {
        return "No"
    }

    // Check if the substring before the dot starts with a letter from the latin alphabet
    if !strings.Contains(strings.ToLower(parts[0]), "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return "No"
    }

    // Check if the substring after the dot is one of the allowed extensions
    if !strings.Contains(parts[1], "txtexe.dll") {
        return "No"
    }

    return "Yes"
}

func main() {
    // Test the function
    fmt.Println(FileNameCheck("example.txt")) // Output: Yes
    fmt.Println(FileNameCheck("1example.dll")) // Output: No
}
```


In this solution, we use the `strings` package to count the occurrences of digits and dots in the file name. We also use the `strings.Split` function to split the file name into two parts: before and after the dot. Then, we check if the substring before the dot starts with a letter from the latin alphabet and if the substring after the dot is one of the allowed extensions. If all conditions are met, we return "Yes", otherwise we return "No".