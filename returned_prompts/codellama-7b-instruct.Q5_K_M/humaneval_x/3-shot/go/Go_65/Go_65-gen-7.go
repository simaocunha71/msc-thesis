    result := ""
    n := len(strconv.Itoa(x))
    if shift > n {
        result = strconv.Itoa(x)[n-1:] + strconv.Itoa(x)[:n-1]
    }else{
        result = strconv.Itoa(x)[n-shift-1:] + strconv.Itoa(x)[:n-shift-1]
    }
    return result
}



