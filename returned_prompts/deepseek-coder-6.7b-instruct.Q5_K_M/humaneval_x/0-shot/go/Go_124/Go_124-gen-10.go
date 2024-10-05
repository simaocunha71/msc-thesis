    if len(date) == 0{
        return false
    }

B:
    date_parts := strings.Split(date, "-")
    if len(date_parts) != 3 {
        return false
    }

C:
    month, err := strconv.Atoi(date_parts[0])
    if err != nil || month < 1 || month > 