    var month, day, year int
    var date_arr = strings.Split(date, "-")
    if len(date_arr) != 3 {
        return false
    }
    if len(date_arr[0]) == 0 || len(date_arr[1]) == 0 || len(date_arr[2]) == 0 {
        return false
    }
    month, _ = strconv.Atoi(date_arr[0])
    day, _ = strconv.Atoi(date_arr[1])
    year, _ = strconv.Atoi(date_arr[2])

    if year < 1000 || year > 3000 {
        return false
    }

    if month < 1 || month > 12 {
        return false
    }

    if day < 1 || day > 31 {
        if (month == 2 && day < 1 || day > 29) || (month != 2 && (month % 2 == 0 && day > 30 || month % 2 == 1 && day > 31)) {
            return false
        }
    }
    return true
}



