    str := strconv.Itoa(x)
    if shift > len(str) {
        revStr := ""
        for _, c := range str {
            revStr = string(c) + revStr
        }
        return revStr
    }
    return str[len(str)-shift:] + str[:len(str)-shift]
}



