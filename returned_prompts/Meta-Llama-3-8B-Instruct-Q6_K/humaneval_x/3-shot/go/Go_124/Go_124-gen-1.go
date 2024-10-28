    if len(date) < 10 {
        return false
    }
    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }
    day, err := strconv.Atoi(parts[1])
    if err != nil || day < 1 || (parts[0] != "02" && day > 31) {
        return false
    }
    month, err := strconv.Atoi(parts[0])
    if err != nil || month < 1 || month > 12 {
        return false
    }
    year, err := strconv.Atoi(parts[2])
    if err != nil {
        return false
    }
    // Check for leap year
    isLeapYear := false
    if year%4 == 0 && (year%100 != 0 || year%400 == 0) {
        isLeapYear = true
    }
    if month == 2 {
        if isLeapYear && day > 29 {
            return false
        } else if !isLeapYear && day > 28 {
            return false
        }
    }
    return true
}