    date = strings.Replace(date,"-"," ",-1)
    parts := strings.Split(date," ")
    month, _ := strconv.Atoi(parts[0])
    day, _ := strconv.Atoi(parts[1])
    year, _ := strconv.Atoi(parts[2])

    if month == 2{
        return day >= 1 && day <= 29
    }else if month == 4 || month == 6 || month == 9 || month == 11{
        return day >= 1 && day <= 30
    }else if month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12{
        return day >= 1 && day <= 31
    }
    return false
}

