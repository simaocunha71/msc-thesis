    if strings.EqualFold(str, strings.Reverse(str)) {
        return str
    }
    for i := len(str) - 1; i >= 0; i-- {
        prefix := str[:i+1]
        postfix := strings.Reverse(prefix)
        if strings.EqualFold(str, prefix+postfix) {
            return str + postfix
        }
    }
    return str + strings.Reverse(str)
}