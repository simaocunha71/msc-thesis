    if date == "" {
        return false
    }

    date_parts := strings.Split(date, "-")
    if len(date_parts) != 3 {
        return false
    }

    month, _ := strconv.Atoi(date_parts[0])
    day, _ := strconv.Atoi(date_parts[1])
    year, _ := strconv.Atoi(date_parts[2])

    if month < 1 || month > 12 || day < 1 || day > 31 || (month == 2 && day > 28) || (month == 4 || month == 6 || month == 9 || month == 11 && day > 30) || (year < 0 || year > 9999) {
        return false
    }

    return true
}



