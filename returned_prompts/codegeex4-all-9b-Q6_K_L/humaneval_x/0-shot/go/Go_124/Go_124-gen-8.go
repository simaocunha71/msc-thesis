```go
func ValidDate(date string) bool {
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
    } else if (month == 4 || month == 6 || month == 9 || month == 11) && day > 30 {
        return false
    }
    return true
}
```