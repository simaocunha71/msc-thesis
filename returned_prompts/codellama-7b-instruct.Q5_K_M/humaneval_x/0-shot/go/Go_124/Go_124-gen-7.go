    if len(date) == 0 {
        return false
    }
    
    dateSlice := strings.Split(date, "-")
    if len(dateSlice) != 3 {
        return false
    }

    month, err := strconv.Atoi(dateSlice[0])
    if err != nil || month < 1 || month > 12 {
        return false
    }

    day, err := strconv.Atoi(dateSlice[1])
    if err != nil || day < 1 || day > 31 {
        return false
    }
    
    year, err := strconv.Atoi(dateSlice[2])
    if err != nil || year < 0 || year > 9999 {
        return false
    }

    if month == 2 {
        if day < 1 || day > 29 {
            return false
        }
    } else if day < 1 || day > 30 {
        return false
    }

    return true
}
