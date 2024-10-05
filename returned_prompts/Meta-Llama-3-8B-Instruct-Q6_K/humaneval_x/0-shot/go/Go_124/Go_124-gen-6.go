Here is a Go solution that uses regular expressions to validate the date format and checks the validity of the date according to the rules:

```go
package main

import (
    "fmt"
    "regexp"
)

func ValidDate(date string) bool {
    // Validate the date format
    dateRegex, _ := regexp.Compile(`^(\d{2})-(\d{2})-(\d{4})$`)
    if !dateRegex.MatchString(date) {
        return false
    }

    // Split the date into month, day, and year
    parts := strings.Split(date, "-")
    month, _ := strconv.Atoi(parts[0])
    day, _ := strconv.Atoi(parts[1])
    year, _ := strconv.Atoi(parts[2])

    // Validate the month
    if month < 1 || month > 12 {
        return false
    }

    // Validate the day
    var validDays [12]int
    validDays[1] = 31
    validDays[3] = 31
    validDays[4] = 30
    validDays[5] = 31
    validDays[6] = 30
    validDays[7] = 31
    validDays[8] = 31
    validDays[9] = 30
    validDays[10] = 31
    validDays[11] = 30
    validDays[12] = 31
    if month == 2 {
        if year%4 == 0 {
            if day > 29 {
                return false
            }
        } else {
            if day > 28 {
                return false
            }
        }
    } else {
        if day < 1 || day > validDays[month-1] {
            return false
        }
    }

    return true
}

func main() {
    fmt.Println(ValidDate("03-11-2000")) // true
    fmt.Println(ValidDate("15-01-2012")) // false
    fmt.Println(ValidDate("04-0-2040")) // false
    fmt.Println(ValidDate("06-04-2020")) // true
    fmt.Println(ValidDate("06/04/2020")) // false
}
```

This program will print the result of the function `ValidDate` for each of the test cases. The function `ValidDate` uses regular expressions to validate the