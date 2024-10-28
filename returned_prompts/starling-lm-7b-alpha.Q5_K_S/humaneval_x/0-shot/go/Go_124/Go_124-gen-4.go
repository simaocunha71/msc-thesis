    // Check format
    if !strings.HasSuffix(date, "-yyyy") {
        return false
    }

    // Convert string to []int
    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }
    months, days, years := parts[0], parts[1], parts[2]
    if _, err := strconv.Atoi(months); err != nil {
        return false
    }
    if _, err := strconv.Atoi(days); err != nil {
        return false
    }
    if _, err := strconv.Atoi(years); err != nil {
        return false
    }

    // Check month range
    month, _ := strconv.Atoi(months)
    if month < 1 || month > 12 {
        return false
    }

    // Check day range
    day, _ := strconv.Atoi(days)
    if month == 2 {
        if day < 1 || day > 29 {
            return false
        }
    } else if month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12 {
        if day < 1 || day > 31 {
            return false
        }
    } else {
        if day < 1 || day > 30 {
            return false
        }
    }

    return true
}






















































































































































