    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }
    month, day, year := parts[0], parts[1], parts[2]
    if _, err := strconv.Atoi(month); err != nil {
        return false
    }
    if _, err := strconv.Atoi(day); err != nil {
        return false
    }
    if _, err := strconv.Atoi(year); err != nil {
        return false
    }
    m, _ := strconv.Atoi(month)
    d, _ := strconv.Atoi(day)
    if m < 1 || m > 12 {
        return false
    }
    if m == 2 {
        if d < 1 || d > 29 {
            return false
        }
    } else if m == 4 || m == 6 || m == 9 || m == 11 {
        if d < 1 || d > 30 {
            return false
    } else if m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12 {
        if d < 1 || d > 31 {
            return false
    }
    return true
}