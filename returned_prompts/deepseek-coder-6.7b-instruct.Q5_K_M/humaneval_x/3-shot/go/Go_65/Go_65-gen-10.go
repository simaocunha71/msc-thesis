    str_x := strconv.Itoa(x)
    if shift >= len(str_x) {
        reverse := ""
        for _, c := range str_x {
            reverse = string(c) + reverse
        }
        return reverse
    } else {
        return str_x[len(str_x)-shift:] + str_x[:len(str_x)-shift]
    }
}



