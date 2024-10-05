    s = strings.Replace(s, c, "", -1)
    if s == Reverse(s) {
        return [2]interface{}{s, true}
    }
    return [2]interface{}{s, false}
}

