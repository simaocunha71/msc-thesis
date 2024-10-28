    if len(date) == 0 {
        return false
    }

    var date_split = strings.Split(date, "-")

    if len(date_split) != 3 {
        return false
    }

    var month, day, year = date_split[0], date_split[1], date_split[2]

    if len(month) == 0 || len(day) == 0 || len(year) == 0 {
        return false
    }

    if month_num, err := strconv.Atoi(month); err != nil {
        return false
    } else if month_num < 1 || month_num > 12 {
        return false
    }

    if day_num, err := strconv.Atoi(day); err != nil {
        return false
    } else if day_num < 1 || day_num > 31 {
        return false
    }

    if year_num, err := strconv.Atoi(year); err != nil {
        return false
    } else if year_num < 0 || year_num > 2040 {
        return false
    }

    return true
}



