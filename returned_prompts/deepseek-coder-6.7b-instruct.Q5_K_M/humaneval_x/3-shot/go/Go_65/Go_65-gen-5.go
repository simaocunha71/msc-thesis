    str_x := strconv.Itoa(x)

    if shift >= len(str_x) {
        return Reverse(str_x)
    }

    return str_x[len(str_x)-shift:] + str_x[:len(str_x)-shift]
}



