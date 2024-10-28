    if len(date) == 0 {
        return false
    }
    dateArr := strings.Split(date, "-")
    if len(dateArr) != 3 {
        return false
    }
    month, _ := strconv.Atoi(dateArr[0])
    day, _ := strconv.Atoi(dateArr[1])
    year, _ := strconv.Atoi(dateArr[2])
    if month < 1 || month > 12 {
        return false
    }
    if day < 1 {
        return false
    }
    if day > 31 && (month != 1 && month != 3 && month != 5 && month != 7 && month != 8 && month != 10 && month != 12) {
        return false
    }
    if day > 30 && (month != 4 && month != 6 && month != 9 && month != 11) {
        return false
    }
    if day > 29 && month == 2 {
        return false
    }
    if year < 1 {
        return false
    }
    return true
}












































































































































































































































