    parts := strings.Split(date,"-")
    if len(parts) != 3 {
        return false
    }

    _, err := strconv.Atoi(parts[0])
    if err != nil {
        return false
    }
    _, err = strconv.Atoi(parts[1])
    if err != nil {
        return false
    }
    _, err = strconv.Atoi(parts[2])
    if err != nil {
        return false
    }

    month, _ := strconv.Atoi(parts[0])
    day, _ := strconv.Atoi(parts[1])
    year, _ := strconv.Atoi(parts[2])

    if month < 1 || month > 12 {
        return false
    }
    if day < 1 {
        return false
    }
    if month == 2 && day > 28 {
        return false
    }
    if month == 2 && day == 29 && !IsLeapYear(year) {
        return false
    }
    if month in [1,3,5,7,8,10,12]:
        if day > 31 {
            return false
        }
    if month in [4,6,9,11]:
        if day > 30 {
            return false
        }

    return true
}



