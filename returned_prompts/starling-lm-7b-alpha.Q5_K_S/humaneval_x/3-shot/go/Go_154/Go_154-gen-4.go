    for _, c := range []string{"", b, b + b, b + b + b} {
        if a = a + c; strings.Contains(a, b) {
            return true
        }
    }
    return false
}



