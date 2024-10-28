    xStr := strconv.Itoa(x)
    n := len(xStr)
    if shift > n {
        return string(reverse(xStr))
    }
    return xStr[n-shift:] + xStr[:n-shift]
}



