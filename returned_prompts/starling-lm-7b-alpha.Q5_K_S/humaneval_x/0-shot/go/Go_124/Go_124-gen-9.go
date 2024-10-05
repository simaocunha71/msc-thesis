    if len(date) == 0 {
        return false
    }

    if len(date) != 10 {
        return false
    }

    if !checkMonth(date) {
        return false
    }

    if !checkDay(date) {
        return false
    }

    return true
}

func checkMonth(date string) bool {
    month, _ := strconv.Atoi(date[0:2])
    if month < 1 || month > 12 {
        return false
    }
    return true
}

func checkDay(date string) bool {
    day, _ := strconv.Atoi(date[3:5])
    if day == 31 && (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
        return false
    }
    if day == 30 && (month == 4 || month == 6 || month == 9 || month == 11) {
        return false
    }
    if day == 29 && month == 2 {
        return false
    }
    return true
}































































































































































































































