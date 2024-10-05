    if len(date) == 0 {
        return false
    }
    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }
    month, _ := strconv.Atoi(parts[0])
    day, _ := strconv.Atoi(parts[1])
    year, _ := strconv.Atoi(parts[2])

    if month < 1 || month > 12 {
        return false
    }
    if day < 1 {
        return false
    }
    if year < 0 {
        return false
    }
    if month == 2 && day > 29 {
        return false
    }
    if month == 4 || month == 6 || month == 9 || month == 11 {
        if day > 30 {
            return false
        }
    }
    if month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12 {
        if day > 31 {
            return false
        }
    }

    return true
}







































































































































































































































