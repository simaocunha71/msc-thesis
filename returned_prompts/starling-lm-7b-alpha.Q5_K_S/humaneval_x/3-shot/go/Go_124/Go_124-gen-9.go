    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }

    month, _ := strconv.Atoi(parts[0])
    day, _ := strconv.Atoi(parts[1])
    year, _ := strconv.Atoi(parts[2])

    if (month < 1 || month > 12) || (day < 1 || day > 31) {
        return false
    }

    if month == 2 && day > 29 {
        return false
    }

    if (month == 4 || month == 6 || month == 9 || month == 11) && day > 30 {
        return false
    }

    return true
}



