    return len(txt) > 0 && !strings.ContainsAny(txt[:len(txt)-1], " ")
}