    x_str := strconv.Itoa(x)
    x_len := len(x_str)
    if shift > x_len{
        shift = shift%x_len
    }
    return x_str[len(x_str)-shift:] + x_str[0:len(x_str)-shift]
}



