    parts := strings.Split(date, "-")
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
    if len(date) == 0 ||
        (month < 1 || month > 12) ||
        (day < 1 || day > 31) ||
        (year < 0 || year > 9999) {
        return false
    }
    switch month {
    case 4, 6, 9, 11:
        if day < 1 || day > 30 {
            return false
        }
    case 2:
        if day < 1 || day > 28 {
            return false
        }
    case 1, 3, 5, 7, 8, 10, 12:
        if day < 1 || day > 31 {
            return false
        }
    }
    return true
}



