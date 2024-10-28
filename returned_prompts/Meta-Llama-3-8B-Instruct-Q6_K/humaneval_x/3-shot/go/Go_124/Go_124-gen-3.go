    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }
    month, day, year := parts[0], parts[1], parts[2]
    month, err := strconv.Atoi(month)
    day, err = strconv.Atoi(day)
    year, err = strconv.Atoi(year)
    if err != nil {
        return false
    }
    if month < 1 || month > 12 {
        return false
    }
    if day < 1 {
        return false
    }
    var maxDays int
    switch {
    case month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12:
        maxDays = 31
    case month == 4 || month == 6 || month == 9 || month == 11:
        maxDays = 30
    case month == 2:
        if (year%4 == 0 && year%100 != 0) || year%400 == 0 {
            maxDays = 29
        } else {
            maxDays = 28
        }
    }
    if day > maxDays {
        return false
    }
    return true
} 