    // Your code goes here
    // split the date string into its parts
    parts := strings.Split(date, "-")

    // check that all parts are present
    if len(parts) != 3 {
        return false
    }

    // convert the string parts to numbers
    month, err1 := strconv.Atoi(parts[0])
    day, err2 := strconv.Atoi(parts[1])
    year, err3 := strconv.Atoi(parts[2])

    // check that all parts are integers
    if err1 != nil || err2 != nil || err3 != nil {
        return false
    }

    // check that the month is in range
    if month < 1 || month > 12 {
        return false
    }

    // check that the day is in range
    switch month {
    case 1, 3, 5, 7, 8, 10, 12:
        if day < 1 || day > 31 {
            return false
        }
    case 4, 6, 9, 11:
        if day < 1 || day > 30 {
            return false
        }
    case 2:
        if day < 1 || day > 29 {
            return false
        }
    }

    // check that the year is in range
    if year < 0 || year > 9999 {
        return false
    }

    // if all checks are passed, return true
    return true
}
