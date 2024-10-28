    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }
    month, day, year := parts[0], parts[1], parts[2]
    if month == "" || day == "" || year == "" {
        return false
    }
    if _, err := strconv.Atoi(month); err != nil {
        return false
    }
    if _, err := strconv.Atoi(day); err != nil {
        return false
    }
    if _, err := strconv.Atoi(year); err != nil {
        return false
    }
    month, day, year = int64(month), int64(day), int64(year)
    if month < 1 || month > 12 {
        return false
    }
    if day < 1 {
        return false
    }
    var daysInMonth = []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
    if month == 2 && day > 29 {
        return false
    } else if month != 2 && (day > daysInMonth[month-1]) {
        return false
    }
    return true
}