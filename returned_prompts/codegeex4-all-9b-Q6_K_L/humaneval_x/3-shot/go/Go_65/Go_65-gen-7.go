    str := strconv.Itoa(x)
    for i := 0; i < shift; i++ {
        str = str[len(str)-1:] + str[0:len(str)-1]
    }
    return str
}

