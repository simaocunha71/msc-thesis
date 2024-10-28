    date = strings.Replace(date,"-"," ",-1)
    date = strings.Replace(date,"/"," ",-1)
    date = strings.TrimSpace(date)
    date = strings.ToLower(date)
    date = strings.Split(date," ")[0]

    date_split := strings.Split(date, " ")

    if len(date_split)!=3 {
        return false
    }

    month, err := strconv.Atoi(date_split[0])
    if err!=nil || month<1 || month>12 {
        return false
    }

    day, err := strconv.Atoi(date_split[1])
    if err!=nil || day<1 {
        return false
    }

    year, err := strconv.Atoi(date_split[2])
    if err!=nil {
        return false
    }

    if month==2 {
        if day>29 {
            return false
        }
    }else if month==4 || month==6 || month==9 || month==11 {
        if day>30 {
            return false
        }
    }else if day>31 {
        return false
    }

    return true
}



