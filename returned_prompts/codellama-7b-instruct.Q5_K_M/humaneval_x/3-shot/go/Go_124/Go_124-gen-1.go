    if len(date) == 0 {
        return false
    }

    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }

    if len(parts[1]) > 2 {
        return false
    }

    if len(parts[2]) != 4 {
        return false
    }

    year, _ := strconv.Atoi(parts[2])
    if year < 1900 || year > 2100 {
        return false
    }

    month, _ := strconv.Atoi(parts[0])
    if month < 1 || month > 12 {
        return false
    }

    day, _ := strconv.Atoi(parts[1])
    if month == 2 {
        if day < 1 || day > 28 {
            return false
        }
    } else if month == 4 || month == 6 || month == 9 || month == 11 {
        if day < 1 || day > 30 {
            return false
        }
    } else if day < 1 || day > 31 {
        return false
    }

    return true
}



