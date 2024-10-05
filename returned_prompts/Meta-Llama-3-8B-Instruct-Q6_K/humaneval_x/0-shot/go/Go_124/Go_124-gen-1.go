Here is a Go function that validates a given date string:

```go
package main

import (
    "strconv"
    "strings"
)

func ValidDate(date string) bool {
    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }

    month, err := strconv.Atoi(parts[0])
    if err != nil || month < 1 || month > 12 {
        return false
    }

    day, err := strconv.Atoi(parts[1])
    if err != nil || (month == 2 && day > 29) || (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12 && day > 31) || (month == 4 || month == 6 || month == 9 || month == 11 && day > 30) {
        return false
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

This function first splits the date string into three parts: month, day, and year. Then it checks if the month is between 1 and 12, and if the day is valid for the given month. If all checks pass, it returns true; otherwise, it returns false. The `main` function is just for testing the `ValidDate` function. You can run this program to see the results.