    s = strings.Replace(s, "apples", "", -1)
    s = strings.Replace(s, "oranges", "", -1)
    s = strings.Replace(s, "and", "", -1)
    s = strings.Replace(s, " ", "", -1)
    
    apples_oranges, _ := strconv.Atoi(s)
    return n - apples_oranges
}


