```go
func ValidDate(date string) bool {
    dateSplit := strings.Split(date, "-")
    if len(dateSplit) != 3 {
        return false
    }
    month, err := strconv.Atoi(dateSplit[0])
    if err != nil {
        return false
    }
    day, err := strconv.Atoi(dateSplit[1])
    if err != nil {
        return false
    }
    year, err := strconv.Atoi(dateSplit[2])
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
        if day == 29 && ((year % 4 != 0) || (year % 100 == 0 && year % 400 != 0)) {
            return false
        }
    }
    return true
}
```
