    if date == "" {
        return false
    }

B:
    dateList := strings.Split(date, "-")
    if len(dateList) != 3 {
        return false
    }

C:
    month, errM := strconv.Atoi(dateList[0])
    day, errD := strconv.Atoi(dateList[1])
    year, errY := strconv.Atoi(dateList[2])

    if errM != nil || errD != nil || errY != nil {
        return false
    }

D:
    if month < 1 || month > 12 {
        return false
    }

E:
    var daysInMonth int
    switch month {
    case 1, 3, 5, 7, 8, 10, 12:
        if day < 1 || day > 31 {
            return false
        }
        daysInMonth = 31
    case 4, 6, 9, 11:
        if day < 1 || day > 30 {
            return false
        }
        daysInMonth = 30
    case 2:
        if (year%4 == 0 && year%100 != 0) || (year%400 == 0) {
            if day < 1 || day > 29 {
                return false
            }
            daysInMonth = 29
        } else {
            if day < 1 || day > 28 {
                return false
            }
            daysInMonth = 28
        }
    default:
        return false
    }

F:
    if day < 1 || day > daysInMonth {
        return false
    }

G:
    return true
}
```

The function `ValidDate` validates the given date string based on the rules mentioned in the question.

1. It first checks if the date is not empty.
2. It then splits the date into month, day and year.
3. It converts the month, day and year to integers. If any of them is not convertible, it returns false.
4. It checks if the month