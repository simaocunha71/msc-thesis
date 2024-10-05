    if date == ""{
        return false
    }

    date_parts := strings.Split(date, "-")
    if len(date_parts) != 3 {
        return false
    }

    month, err := strconv.Atoi(date_parts[0])
    if err != nil {
        return false
    }
    day, err := strconv.Atoi(date_parts[1])
    if err != nil {
        return false
    }
    year, err := strconv.Atoi(date_parts[2])
    if err != nil {
        return false
    }

    if month < 1 || month > 12 {
        return false
    }

    if day < 1 || day > 31 {
        return false
    }

    if day > 30 && month == 2 {
        return false
    }

    if day > 30 && (month == 4 || month == 6 || month == 9 || month == 11) {
        return false
    }

    if day > 31 && (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
        return false
    }

    return true
}



