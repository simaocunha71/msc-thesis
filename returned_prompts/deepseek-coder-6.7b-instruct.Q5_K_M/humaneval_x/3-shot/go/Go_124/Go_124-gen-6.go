    if len(date) == 0 {
        return false
    }

    split := strings.Split(date, "-")
    if len(split) != 3 {
        return false
    }

    month, err1 := strconv.Atoi(split[0])
    day, err2 := strconv.Atoi(split[1])
    year, err3 := strconv.Atoi(split[2])

    if err1 != nil || err2 != nil || err3 != nil {
        return false
    }

    if month < 1 || month > 12 {
        return false
    }

    if day < 1 || day > 31 {
        return false
    }

    if month == 4 || month == 6 || month == 9 || month == 11 {
        if day > 30 {
            return false
        }
    }

    if month == 2 {
        if day > 29 {
            return false
        }
    }

    return true
}



