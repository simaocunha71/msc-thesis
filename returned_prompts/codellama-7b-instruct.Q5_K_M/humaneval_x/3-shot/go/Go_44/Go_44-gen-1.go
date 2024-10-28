    if x < base {
        return strconv.Itoa(x)
    }
    return ChangeBase(x / base, base) + strconv.Itoa(x % base)
}



