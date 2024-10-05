    splitted := strings.Split(s, "and")
    sum, _ := strconv.Atoi(strings.Split(splitted[0], " ")[0])
    return n - sum
}



