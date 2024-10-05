    if s == "0 apples and 0 oranges"{
        return n
    }
    var apples, oranges int
    var apples_string string
    var oranges_string string
    for _,v := range strings.Split(s, "and") {
        if strings.Contains(v, "apples"){
            apples_string = strings.Split(v, "apples")[0]
            apples,_ = strconv.Atoi(apples_string)
        } else {
            oranges_string = strings.Split(v, "oranges")[0]
            oranges,_ = strconv.Atoi(oranges_string)
        }
    }
    return n - apples - oranges
}



