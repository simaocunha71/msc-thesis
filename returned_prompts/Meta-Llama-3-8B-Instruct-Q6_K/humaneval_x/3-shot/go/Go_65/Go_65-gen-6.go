    str := strconv.Itoa(x)
    n := len(str)

    shift = shift % n
    if shift == 0 {
        return str
    }

    return str[n-shift:] + str[:n-shift]
}