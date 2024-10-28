    if date == "" {
        return false
    }

B:
    splitted := strings.Split(date, "-")
    if len(splitted) != 3 {
        return false
    }

C:
    month, errM := strconv.Atoi(splitted[0])
    day, errD := strconv.Atoi(splitted[1])
    year, errY := strconv.Atoi(splitted[2])

    if errM != nil || errD != nil || errY != nil {
        return false
    }

D:
    if month < 1 || month > 12 {
        return false
    }

E:
    if month == 2 {
        if day < 1 || day > 29 {
            return false
        }
    } else if month == 4 || month == 6 || month == 9 || month == 11 {
        if day < 1 || day > 30 {
            return false
        }
    } else {
        if day < 1 || day > 31 {
            return false
        }
    }

F:
    if year < 1 {
        return false
    }

G:
    return true
}



























































































































































































































