    var parts []string
    parts = strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }
    var month_num, day_num int
    if month_num, err := strconv.Atoi(parts[0]); err != nil {
        return false
    } else if day_num, err := strconv.Atoi(parts[1]); err != nil {
        return false
    } else {
        if month_num < 1 || month_num > 12 || day_num < 1 {
            return false
        }
        if month_num == 2 && day_num > 29 {
            return false
        }
        if month_num == 1 || month_num == 3 || month_num == 5 || month_num == 7 || month_num == 8 || month_num == 10 || month_num == 12 {
            if day_num > 31 {
                return false
            }
        }
        if month_num == 4 || month_num == 6 || month_num == 9 || month_num == 11 {
            if day_num > 30 {
                return false
            }
        }
    }
    if _, err := strconv.Atoi(parts[2]); err != nil {
        return false
    }
    return true
}



