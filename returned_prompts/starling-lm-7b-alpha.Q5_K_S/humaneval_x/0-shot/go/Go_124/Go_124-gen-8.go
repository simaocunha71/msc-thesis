    // Split the date string into its three parts
    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }

    // Convert the parts to integers
    month, _ := strconv.Atoi(parts[0])
    day, _ := strconv.Atoi(parts[1])
    year, _ := strconv.Atoi(parts[2])

    // Check if the year is not before 0
    if year < 0 {
        return false
    }

    // Check if the month is not before 1 or after 12
    if month < 1 || month > 12 {
        return false
    }

    // Check if the day is not before 1 or after the max days of the month
    switch month {
    case 2:
        if day < 1 || day > 29 {
            return false
        }
    case 1, 3, 5, 7, 8, 10, 12:
        if day < 1 || day > 31 {
            return false
        }
    case 4, 6, 9, 11:
        if day < 1 || day > 30 {
            return false
        }
    }

    return true
}



































































































































































































