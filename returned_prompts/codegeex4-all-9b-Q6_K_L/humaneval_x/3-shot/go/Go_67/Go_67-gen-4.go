    s = strings.ReplaceAll(s," ","")
    n_apples, _ := strconv.Atoi(s[0:strings.Index(s, "apples")])
    n_oranges, _ := strconv.Atoi(s[strings.Index(s, "and")+3:])
    return n - n_apples - n_oranges
}