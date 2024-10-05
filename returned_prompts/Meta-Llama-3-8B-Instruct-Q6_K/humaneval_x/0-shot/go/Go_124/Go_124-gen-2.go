Here is the solution for the problem:

```go
package main

import (
    "fmt"
    "strconv"
    "strings"
)

func ValidDate(date string) bool {

    // Split the date string into three parts: month, day, and year
    parts := strings.Split(date, "-")

    // Check if the date string is not empty
    if len(parts) != 3 {
        return false
    }

    // Convert the month, day, and year to integers
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

    // Check if the month is not less than 1 or higher than 12
    if month < 1 || month > 12 {
        return false
    }

    // Check if the day is valid for the given month
    switch month {
    case 1, 3, 5, 7, 8, 10, 12:
        if day < 1 || day > 31 {
            return false
        }
    case 4, 6, 9, 11:
        if day < 1 || day > 30 {
            return false
        }
    case 2:
        if day < 1 || day > 29 {
            return false
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

In this solution, we first split the date string into three parts: month, day, and year. Then we convert these parts to integers. We then check if the month is not less than 1 or higher than 12. After that, we check if the day is valid for the given month. We use a switch statement to check the month and return false if the day is not valid. Finally, we return true if the