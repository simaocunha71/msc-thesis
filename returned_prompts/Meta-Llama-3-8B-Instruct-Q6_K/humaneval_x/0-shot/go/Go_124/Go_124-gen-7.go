Here is a Go solution for the problem:

```go
package main

import (
    "fmt"
    "strconv"
    "strings"
)

func ValidDate(date string) bool {
    // Split the date string into parts
    parts := strings.Split(date, "-")

    // Check if the date string is not empty
    if len(parts) != 3 {
        return false
    }

    // Parse the month, day and year
    month, err := strconv.Atoi(parts[0])
    if err != nil {
        return false
    }
    day, err := strconv.Atoi(parts[1])
    if err != nil {
        return false
    }
    year, err := strconv.Atoi(parts[2])
    if err != nil {
        return false
    }

    // Check if the date is valid
    if month < 1 || month > 12 {
        return false
    }
    if month == 2 {
        if day < 1 || day > 29 {
            return false
        }
    } else if month == 4 || month == 6 || month == 9 || month == 11 {
        if day < 1 || day > 30 {
            return false
    } else {
        if day < 1 || day > 31 {
            return false
        }
    }

    // Check if the year is valid
    if year < 1 {
        return false
    }

    // If all checks pass, the date is valid
    return true
}

func main() {
    fmt.Println(ValidDate("03-11-2000"))  // true
    fmt.Println(ValidDate("15-01-2012"))  // false
    fmt.Println(ValidDate("04-0-2040"))   // false
    fmt.Println(ValidDate("06-04-2020"))  // true
    fmt.Println(ValidDate("06/04/2020"))  // false
}
```

This program splits the date string into parts, parses each part into an integer, and then checks if the date is valid based on the rules provided. If the date is valid, it returns true; otherwise, it returns false. The `main` function tests the `ValidDate` function with different date strings.