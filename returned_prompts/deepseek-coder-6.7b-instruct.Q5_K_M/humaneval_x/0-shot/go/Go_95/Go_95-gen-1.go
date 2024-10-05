    for key := range dict {
        switch key := key.(type) {
        case string:
            if strings.ToUpper(key) == key {
                hasUpper = true
            } else if strings.ToLower(key) == key {
                hasLower = true
            } else {
                return false
            }
        default:
            return false
        }

        if hasLower && hasUpper {
            break A
        }
    }

    return hasLower != hasUpper
}

This function keeps track of whether it has seen a key in lower case and in upper case. If it finds a non-string key, it returns false. If it finds a key in either case, it sets the corresponding variable