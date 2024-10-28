    if strings.HasPrefix(date, "/") {
        return false
    }
    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }
    month, day, year := parts[0], parts[1], parts[2]
    if len(month) < 2 || len(day) < 2 || len(year) < 4 {
        return false
    }
    if _, err := strconv.Atoi(month); err != nil {
        return false
    }
    if _, err := strconv.Atoi(day); err != nil {
        return false
    }
    if _, err := strconv.Atoi(year); err != nil {
        return false
    }
    monthInt, _ := strconv.Atoi(month)
    dayInt, _ := strconv.Atoi(day)
    if monthInt < 1 || monthInt > 12 {
        return false
    }
    if monthInt == 2 {
        if dayInt > 29 {
            return false
        }
    } else if monthInt == 4 || monthInt == 6 || monthInt == 9 || monthInt == 11 {
        if dayInt > 30 {
            return false
        }
    } else {
        if dayInt > 31 {
            return false
        }
    }
    return true
}