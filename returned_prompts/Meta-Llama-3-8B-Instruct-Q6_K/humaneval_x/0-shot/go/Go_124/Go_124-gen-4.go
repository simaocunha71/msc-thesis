Here is the Go code that solves the problem:

```go
package main

import (
    "fmt"
    "strings"
    "time"
)

func ValidDate(date string) bool {
    // Split the date string into month, day and year
    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }

    // Check if the date string is in the correct format
    _, err := time.Parse("01-02-2006", date)
    if err != nil {
        return false
    }

    // Parse the date into a time.Time object
    t, err := time.Parse("01-02-2006", date)
    if err != nil {
        return false
    }

    // Check if the date is valid
    if t.Year() < 1000 || t.Year() > 9999 {
        return false
    }
    if t.Month() < 1 || t.Month() > 12 {
        return false
    }
    if t.Day() < 1 {
        return false
    }
    if t.Day() > 31 {
        switch t.Month() {
        case 1, 3, 5, 7, 8, 10, 12:
            return false
        case 4, 6, 9, 11:
            if t.Day() > 30 {
                return false
            }
        case 2:
            if t.Day() > 29 {
                return false
            }
        }
    }

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

This code first checks if the date string is in the correct format. If it's not, it returns false. Then it parses the date into a time.Time object and checks if the date is valid according to the rules specified in the problem. If the date is valid, it returns true; otherwise, it returns false. The main function tests the ValidDate function with different date strings. The results are printed to the console.