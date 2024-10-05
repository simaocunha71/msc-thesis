```go
func ValidDate(date string) bool {
    if len(date) != 10 || date[2] != '-' || date[5] != '-' {
        return false
    }
    month, err := strconv.Atoi(date[0:2])
    if err != nil || month < 1 || month > 12 {
        return false
    }
    day, err := strconv.Atoi(date[3:5])
    if err != nil || day < 1 || day > 31 {
        return false
    }
    year, err := strconv.Atoi(date[6:])
    if err != nil {
        return false
    }
    if month == 2 {
        if year%4 == 0 && (year%100 != 0 || year%400 == 0) {
            if day > 29 {
                return false
            }
        } else if day > 28 {
            return false
        }
    } else if month == 4 || month == 6 || month == 9 || month == 11 {
        if day > 30 {
            return false
        }
    }
    return true
}
```