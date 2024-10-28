    for _, rotation := range []string {b, b + b, b + b + b, b + b + b + b} {
        if strings.Contains(a, rotation) {
            return true
        }
    }
    return false
}



