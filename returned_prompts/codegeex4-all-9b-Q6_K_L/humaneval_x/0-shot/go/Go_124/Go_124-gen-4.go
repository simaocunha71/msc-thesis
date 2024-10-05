```go
func ValidDate(date string) bool {
    // check if date is empty
    if date == "" {
        return false
    }
    // check if date is in the correct format
    if len(date) != 10 || date[2] != '-' || date[5] != '-' {
        return false
    }
    // split date into month, day and year
    month, err := strconv.Atoi(date[0:2])
    if err != nil {
        return false
    }
    day, err := strconv.Atoi(date[3:5])
    if err != nil {
        return false
    }
    year, err := strconv.Atoi(date[6:])
    if err != nil {
        return false
    }
    // check if month is in the correct range
    if month < 1 || month > 12 {
        return false
    }
    // check if day is in the correct range for the given month
    if month == 2 {
        if day < 1 || day > 29 {
            return false
        }
    } else if month == 4 || month == 6 || month == 9 || month == 11 {
        if day < 1 || day > 30 {
            return false
        }
    } else {
        if day < 1 || day > 31 {
            return false
        }
    }
    return true
}
```
