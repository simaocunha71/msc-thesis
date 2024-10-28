Here is a Go solution for the problem:

```go
import (
    "strconv"
    "strings"
)

func ValidDate(date string) bool {
    // Split the date string into month, day, and year
    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }

    // Convert the month, day, and year to integers
    month, err := strconv.Atoi(parts[0])
    if err != nil || month < 1 || month > 12 {
        return false
    }
    day, err := strconv.Atoi(parts[1])
    if err != nil || (month == 2 && day > 29) || (month == 4 || month == 6 || month == 9 || month == 11 && day > 30) || (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12 && day > 31) {
        return false
    }
    year, err := strconv.Atoi(parts[2])
    if err != nil {
        return false
    }

    return true
}
```

This function splits the input date string into month, day, and year, and then checks if each part is a valid integer. It also checks the validity of the month and day based on the rules you provided. If any part of the date is invalid, the function returns false. Otherwise, it returns true.