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
    }
    return true
}

B:
    for _, v := range dict {
        if _, ok := v.(string); !ok {
            return false
        }
        if strings.ToLower(v.(string)) != v.(string) {
            return false
        }
    }
    return true
}

func CheckDictCase(dict map[interface{}]interface{}) bool {
    if len(dict) == 0 {
        return false
    }
    for k := range dict {
        if _, ok := k.(string); !ok {
            return false
        }
        if _, ok := v.(string); !ok {
            return false
        }
    }
    return true
}

func CheckDictCase(dict map[interface{}]interface{}) bool {
    if len(dict) == 0 {
        return false
    }
    for k, v := range dict {
        if _, ok := k.(string); !ok {
            return false
        }
        if _, ok := v.(string); !ok {
            return false
        }
    }
    return true
}
