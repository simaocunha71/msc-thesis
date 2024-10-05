    if date == "" {
        return false
    }
    if len(date) != 10 {
        return false
    }
    if (date[2] == '-' && date[5] == '-'){
        return false
    }
    if (date[2] == '/' && date[5] == '/'){
        return false
    }
    if (date[2] != '-' && date[5] != '-'){
        return false
    }
    if date[8] != '-' && date[8] != '-'{
        return false
    }
    if date[10] == '-' {
        return false
    }
    if date[10] != '-' {
        return false
    }
    if date[0] == '0' || date[1] == '0' || date[3] == '0' || date[4] == '0' || date[6] == '0' || date[7] == '0' || date[9] == '0' {
        return false
    }
    if date[1] == '-' && date[2] == '0' && date[0] == '0' {
        return false
    }
    if date[3] == '-' && date[4] == '0' && date[0] == '0' {
        return false
    }
    if date[6] == '-' && date[7] == '0' && date[0] == '0' {
        return false
    }
    if date[9] == '-' && date[10] == '0' && date[0] == '0' {
        return false
    }
    if date[0] == '0' && date[1] == '0' && date[3] == '0' && date[4] == '0' && date[6] == '0' && date[7] == '0' && date[9] == '0' {
        return false
    }

    month, err := strconv.Atoi(date[0:2])
    if err != nil {
        return false
    }
    day, err := strconv.A