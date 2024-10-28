    for key := range dict {
        _, ok := key.(string)
        if !ok {
            return false
        }
        if len(dict) == 1 {
            return true
        }
        if strings.ToLower(key.(string)) != key.(string) &&
            strings.ToUpper(key.(string)) != key.(string) {
            return false
        }
    }
    return true
}

B:
    for key := range dict {
        if _, ok := key.(string); !ok {
            return false
        }
        if strings.ToLower(key.(string)) != key.(string) &&
            strings.ToUpper(key.(string)) != key.(string) {
            return false
        }
    }
    return true
}

C:
    for _, key := range dict {
        if _, ok := key.(string); !ok {
            return false
        }
        if strings.ToLower(key.(string)) != key.(string) &&
            strings.ToUpper(key.(string)) != key.(string) {
            return false
        }
    }
    return true
}

D:
    for key := range dict {
        if _, ok := key.(string); !ok {
            return false
        }
    }
    for _, key := range dict {
        if strings.ToLower(key.(string)) != key.(string) &&
            strings.ToUpper(key.(string)) != key.(string) {
            return false
        }
    }
    return true
}

E:
    for key := range dict {
        if _, ok := key.(string); !ok {
            return false
        }
    }
    for _, key := range dict {
        if strings.ToLower(key.(string)) != key.(string) ||
            strings.ToUpper(key.(string)) != key.(string) {
            return false
        }
    }
    return true
}

F:
    for key := range dict {
        if _, ok := key.(string); !ok {
            return false
        }
    }
    for _, key := range dict {
        if strings.ToLower(key.(string)) !=