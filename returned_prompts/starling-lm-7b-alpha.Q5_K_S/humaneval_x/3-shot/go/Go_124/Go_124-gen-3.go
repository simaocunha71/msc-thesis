    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }
    month, _ := strconv.Atoi(parts[0])
    day, _ := strconv.Atoi(parts[1])
    year, _ := strconv.Atoi(parts[2])
    if month < 1 || month > 12 || day < 1 {
        return false
    }
    if year < 0 {
        return false
    }
    switch month {
    case 1,3,5,7,8,10,12:
        if day > 31 {
            return false
        }
    case 4,6,9,11:
        if day > 30 {
            return false
        }
    case 2:
        if year % 4 != 0 {
            if day > 28 {
                return false
            }
        } else {
            if day > 29 {
                return false
            }
        }
    }
    return true
}



