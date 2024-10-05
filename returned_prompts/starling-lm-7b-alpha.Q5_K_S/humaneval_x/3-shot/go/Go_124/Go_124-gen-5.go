    parts := strings.Split(date,"-")
    month, _ := strconv.Atoi(parts[0])
    day, _ := strconv.Atoi(parts[1])
    year, _ := strconv.Atoi(parts[2])

    if len(date) == 0 {
        return false
    }

    if len(parts) != 3 {
        return false
    }

    if month < 1 || month > 12 {
        return false
    }

    if day < 1 {
        return false
    }

    if day > 31 && (month != 2 && month != 4 && month != 6 && month != 9 && month != 11) {
        return false
    }

    if day > 30 && (month != 2 && month != 4 && month != 6 && month != 9 && month != 11) {
        return false
    }

    if day > 29 && month == 2 {
        return false
    }

    if year < 0 {
        return false
    }

    return true
}



