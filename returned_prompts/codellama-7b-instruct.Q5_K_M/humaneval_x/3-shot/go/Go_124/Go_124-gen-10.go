    if len(date) == 0{
        return false
    }

    if strings.ContainsAny(date, "/"){
        return false
    }

    date_parts := strings.Split(date, "-")
    if len(date_parts) != 3{
        return false
    }

    month, err := strconv.Atoi(date_parts[0])
    if err != nil || month < 1 || month > 12{
        return false
    }

    day, err := strconv.Atoi(date_parts[1])
    if err != nil || (day < 1 || (month < 7 && month%2 == 0 && day > 31) || (month < 7 && month%2 != 0 && day > 30) || (month == 2 && day > 29)) {
        return false
    }

    year, err := strconv.Atoi(date_parts[2])
    if err != nil || year < 0 {
        return false
    }

    return true
}



