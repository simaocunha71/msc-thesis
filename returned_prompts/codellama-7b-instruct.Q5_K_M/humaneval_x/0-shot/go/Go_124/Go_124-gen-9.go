    if date == "" {
        return false
    }

    splits := strings.Split(date, "-")
    if len(splits) != 3 {
        return false
    }

    month, _ := strconv.Atoi(splits[0])
    day, _ := strconv.Atoi(splits[1])
    year, _ := strconv.Atoi(splits[2])

    if month < 1 || month > 12 {
        return false
    }

    if day < 1 || day > 31 {
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
    } else if day < 1 || day > 31 {
        return false
    }

    return true

}
