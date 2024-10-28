for k, v := range dict {
    if _, ok := k.(string); !ok {
        return false
    }
    if _, ok := v.(string); !ok {
        return false
    }

    if strings.ToLower(k.(string)) != k.(string) {
        return false
    }
    if strings.ToLower(v.(string)) != v.(string) {
        return false
    }

    if len(dict) == 0 {
        return false
    }
}
return true
}
