Here is the solution in Go:
```go
package main

import (
    "fmt"
    "strconv"
    "strings"
)

func ValidDate(date string) bool {
    if len(date) != 10 {
        return false
    }
    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }
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
    if month < 1 || month > 12 {
        return false
    }
    if day < 1 || day > 31 {
        return false
    }
    if month == 2 {
        if day > 29 {
            return false
        }
    } else if month == 4 || month == 6 || month == 9 || month == 11 {
        if day > 30 {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(ValidDate("03-11-2000"))  // true
    fmt.Println(ValidDate("15-01-2012"))  // false
    fmt.Println(ValidDate("04-0-2040"))    // false
    fmt.Println(ValidDate("06-04-2020"))  // true
    fmt.Println(ValidDate("06/04/2020"))  // false
}
```
This function first checks if the length of the input date string is 10. If not, it returns false. Then it splits the date string into three parts using the "-" character as the separator. If the number of parts is not 3, it returns false. Then it converts each part into an integer using the strconv.Atoi function. If any of the conversions fail, it returns false. Then it checks if the month is within the range 1-12, and if the day is within the range 1-31. If the month is February, it also checks if the day is within the range 1-29. If any of these checks fail, it returns false. If all the checks pass, it returns true. The main function tests the ValidDate function with some sample inputs and prints the results.