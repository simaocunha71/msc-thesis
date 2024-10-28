func ChangeBase(x int, base int) string {
    if base < 2 || base > 9 {
        return ""
    }
    return strconv.FormatInt(int64(x), base)
}

B:
func ChangeBase(x int, base int) string {
    if base < 2 || base > 9 {
        return ""
    }
    result := ""
    for x > 0 {
        result = strconv.Itoa(x%base) + result
        x /= base
    }
    return result
}

C:
func ChangeBase(x int, base int) string {
    if base < 2 || base > 9 {
        return ""
    }
    result := ""
    for x > 0 {
        result = string('0' + x%base) + result
        x /= base
    }
    return result
}

D:
func ChangeBase(x int, base int) string {
    if base < 2 || base > 9 {
        return ""
    }
    result := ""
    for x > 0 {
        result = string('0' + x%base) + result
        x /= base
    }
    return result
}