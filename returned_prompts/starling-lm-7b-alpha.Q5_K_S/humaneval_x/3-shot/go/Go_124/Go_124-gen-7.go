    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }
    _, err := strconv.Atoi(parts[0])
    if err != nil {
        return false
    }
    _, err = strconv.Atoi(parts[1])
    if err != nil {
        return false
    }
    _, err = strconv.Atoi(parts[2])
    if err != nil {
        return false
    }
    month, _ := strconv.Atoi(parts[0])
    day, _ := strconv.Atoi(parts[1])
    year, _ := strconv.Atoi(parts[2])
    switch month {
    case 2:
        if day > 29 {
            return false
        }
    case 4, 6, 9, 11:
        if day > 30 {
            return false
        }
    default:
        if day > 31 {
            return false
        }
    }
    return true
}




