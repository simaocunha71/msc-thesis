    str := strconv.Itoa(x)
    shift = shift % len(str)
    if shift == 0 {
        return str
    }
    return str[shift:] + str[:shift]
} 



