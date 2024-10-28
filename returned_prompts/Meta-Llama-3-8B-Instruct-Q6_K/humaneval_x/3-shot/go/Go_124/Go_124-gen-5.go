    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }
    if len(parts[0]) != 2 || len(parts[1]) != 2 || len(parts[2]) != 4 {
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
    if day < 1 {
        return false
    }
    if month == 2 {
        if day > 29 {
            return false
        }
    } else if month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12 {
        if day > 31 {
            return false
        }
    } else {
        if day > 30 {
            return false
        }
    }
    return true
}