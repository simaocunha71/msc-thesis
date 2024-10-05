    var months = [...]int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
    var seperator = "-"

    if date == "" {
        return false
    }

    splits := strings.Split(date, seperator)

    if len(splits) != 3 {
        return false
    }

    month, err := strconv.Atoi(splits[0])
    if err != nil {
        return false
    }

    day, err := strconv.Atoi(splits[1])
    if err != nil {
        return false
    }

    year, err := strconv.Atoi(splits[2])
    if err != nil {
        return false
    }

    if month < 1 || month > 12 {
        return false
    }

    if day < 1 || day > months[month-1] {
        return false
    }

    if month == 2 && day > 28 {
        return false
    }

    if day == 29 && (year%4 != 0 || year%100 == 0 && year%400 != 0) {
        return false
    }

    return true
}



