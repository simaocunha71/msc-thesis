```go
func ValidDate(date string) bool {
    dateParts := strings.Split(date, "-")
    if len(dateParts) != 3 {
        return false
    }
    month, err := strconv.Atoi(dateParts[0])
    if err != nil || month < 1 || month > 12 {
        return false
    }
    day, err := strconv.Atoi(dateParts[1])
    if err != nil || day < 1 {
        return false
    }
    year, err := strconv.Atoi(dateParts[2])
    if err != nil || year < 1 {
        return false
    }
    if month == 2 {
        if day > 29 {
            return false
        } else if day == 29 && (year%400 != 0 || (year%100 == 0 && year%4 != 0)) {
            return false
        }
    } else if (month == 4 || month == 6 || month == 9 || month == 11) && day > 30 {
        return false
    } else if day > 31 {
        return false
    }
    return true
}
```
