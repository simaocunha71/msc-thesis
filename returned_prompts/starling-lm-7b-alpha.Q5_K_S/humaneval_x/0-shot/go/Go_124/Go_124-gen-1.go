date = strings.Split(date, "-")
if len(date) != 3 {
    return false
}

month, day, year := 0, 0, 0

month, _ = strconv.Atoi(date[0])
day, _ = strconv.Atoi(date[1])
year, _ = strconv.Atoi(date[2])

if month < 1 || month > 12 || day < 1 || day > 31 ||
    (month == 2 && day > 29) || year < 0 {
    return false
}

if month == 2 && day == 29 {
    return true
}

if month == 4 || month == 6 || month == 9 || month == 11 {
    if day < 1 || day > 30 {
        return false
    }
} else {
    if day < 1 || day > 31 {
        return false
    }
}

if month == 2 && year % 4 != 0 {
    return false
}

return true
}

























































































































































































































































