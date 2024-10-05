    s := strconv.Itoa(x)
    r := []rune(s)
    if shift > len(r) {
        return string(reverse(r))
    } else {
        return string(r[len(r)-shift:] + r[:len(r)-shift])
    }
}



