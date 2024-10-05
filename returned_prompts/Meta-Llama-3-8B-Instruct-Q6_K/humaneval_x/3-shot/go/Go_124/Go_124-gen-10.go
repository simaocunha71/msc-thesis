    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }
    day, month, year := strconv.Atoi(parts[1]), strconv.Atoi(parts[0]), strconv.Atoi(parts[2])
    if day < 1 || day > 31 {
        return false
    }
    if month < 1 || month > 12 {
        return false
    }
    if month == 2 {
        if day < 1 || day > 29 {
            return false
        }
    } else if month == 4 || month == 6 || month == 9 || month == 11 {
        if day < 1 || day > 30 {
            return false
        }
    } else {
        if day < 1 || day > 31 {
            return false
        }
    }
    return true
}