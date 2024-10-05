    var apples int = 0
    var oranges int = 0
    var mango int = 0
    var err error
    s = strings.Replace(s, "apples", "", -1)
    apples, err = strconv.Atoi(s)
    if err != nil {
        panic(err)
    }
    s = strings.Replace(s, "oranges", "", -1)
    oranges, err = strconv.Atoi(s)
    if err != nil {
        panic(err)
    }
    mango = n - (apples + oranges)
    return mango
}



