    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }
    day, month, year := parts[1], parts[0], parts[2]
    if _, err := strconv.Atoi(day); err != nil {
        return false
    }
    if _, err := strconv.Atoi(month); err != nil {
        return false
    }
    if _, err := strconv.Atoi(year); err != nil {
        return false
    }
    dayInt, _ := strconv.Atoi(day)
    monthInt, _ := strconv.Atoi(month)
    if monthInt < 1 || monthInt > 12 {
        return false
    }
    if monthInt == 2 {
        if dayInt < 1 || dayInt > 29 {
            return false
        }
    } else if monthInt == 4 || monthInt == 6 || monthInt == 9 || monthInt == 11 {
        if dayInt < 1 || dayInt > 30 {
            return false
        }
    } else {
        if dayInt < 1 || dayInt > 31 {
            return false
        }
    }
    return true
}