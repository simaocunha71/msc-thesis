    return strings.Contains(a,b) || strings.Contains(a, b[1:] + b[:1])
}