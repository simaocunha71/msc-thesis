```go
func ValidDate(date string) bool {
    if strings.Count(date, "-") != 2 {
        return false
    }
    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }
    month, err := strconv.Atoi(parts[0])
    if err != nil || month < 1 || month > 12 {
        return false
    }
    day, err := strconv.Atoi(parts[1])
    if err != nil || day < 1 {
        return false
    }
    year, err := strconv.Atoi(parts[2])
    if err != nil {
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
    } else {
        if day > 31 {
            return false
        }
    }
    return true
}
```
