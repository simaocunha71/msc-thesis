    strX := strconv.Itoa(x)
    shift %= len(strX)
    return strX[len(strX)-shift:] + strX[:len(strX)-shift]
}

