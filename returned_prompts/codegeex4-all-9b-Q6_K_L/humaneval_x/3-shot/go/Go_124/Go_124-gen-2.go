    date = strings.Replace(date,"-"," ",-1)
    date = strings.Replace(date,"/"," ",-1)
    date = strings.Replace(date," ","-",1)
    date = strings.Replace(date," ","-",1)

    date_parts := strings.Split(date,"-")

    if len(date_parts) != 3{
        return false
    }

    month,_ := strconv.Atoi(date_parts[0])
    day,_ := strconv.Atoi(date_parts[1])
    year,_ := strconv.Atoi(date_parts[2])

    if month < 1 || month > 12{
        return false
    }

    if day < 1 || day > 31{
        return false
    }

    if month == 2{
        if day > 29{
            return false
        }
    }

    if day > 30{
        if month != 4 && month != 6 && month != 9 && month != 11{
            return false
        }
    }

    if year < 1000 || year > 9999{
        return false
    }

    return true
}