    if len(date) == 0 {
        return false
    }

    parts := strings.Split(date, "-")
    if len(parts) != 3 {
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

    if day < 1 || day > 31 {
        return false
    }

    if year < 1970 || year > 2030 {
        return false
    }

    // TODO: implement the rest of the validations
    return true
}
