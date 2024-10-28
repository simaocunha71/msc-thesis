    if date == "" {
        return false
    }

    // split date into month, day, year
    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }

    // check month, day, year
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

    // February
    if month == 2 && (day < 1 || day > 29) {
        return false
    }

    // April, June, September, November
    if month == 4 || month == 6 || month == 9 || month == 11 {
        if day < 1 || day > 30 {
            return false
        }
    }

    // February
    if month == 2 && day > 28 {
        return false
    }

    // non-leap year
    if year%4 != 0 && month == 2 {
        if day > 28 {
            return false
        }
    }

    return true
}
