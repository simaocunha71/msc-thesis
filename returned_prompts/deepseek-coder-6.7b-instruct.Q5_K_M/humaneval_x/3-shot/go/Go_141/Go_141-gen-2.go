    if count := strings.Count(file_name, "."); count > 1 || count == 0 {
        return "No"
    }

    split := strings.Split(file_name, ".")
    if len(split) != 2 || len(split[0]) == 0 || len(split[1]) != 3 {
        return "No"
    }

    if !((split[1][0] >= 'a' && split[1][0] <= 'z') || (split[1][0] >= 'A' && split[1][0] <= 'Z')) {
        return "No"
    }

    if split[0][0] < '0' || (split[0][0] > '9' && split[0][0] < 'A') || (split[0][0] > 'Z' && split[0][0] < 'a') || split[0][0] > 'z' {
        return "No"
    }

    if count := strings.Count(split[0], ""); count > 3 {
        return "No"
    }

    return "Yes"
}



