    if base > 10{
        panic("Base must be less than 10")
    }
    if x == 0{
        return "0"
    }

    var result string
    for x != 0{
        result = strconv.Itoa(x%base) + result
        x /= base
    }
    return result
}



