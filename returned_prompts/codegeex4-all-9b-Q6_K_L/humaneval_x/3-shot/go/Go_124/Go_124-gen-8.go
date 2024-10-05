    date_parts := strings.Split(date, "-")
    if len(date_parts) != 3 {
        return false
    }

    month, err := strconv.Atoi(date_parts[0])
    if err != nil || month < 1 || month > 12 {
        return false
    }

    day, err := strconv.Atoi(date_parts[1])
    if err != nil || day < 1 {
        return false
    }

    year, err := strconv.Atoi(date_parts[2])
    if err != nil {
        return false
    }

    if month == 2 {
        if day > 29 {
            return false
        }
        if day == 29 && !isLeapYear(year) {
            return false
        }
    } else if month == 4 || month == 6 || month == 9 || month == 11 {
        if day > 30 {
            return false
        }
    } else if day > 31 {
        return false
    }

    return true
}

func isLeapYear(year int) bool {
    if year%4 != 0 {
        return false
    } else if year%100 != 0 {
        return true
    } else if year%400 != 0 {
        return false
    } else {
        return true
    }
}



