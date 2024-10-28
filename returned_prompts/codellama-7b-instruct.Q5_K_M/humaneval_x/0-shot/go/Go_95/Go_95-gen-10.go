    for key, val := range dict {
        if !strings.HasPrefix(fmt.Sprintf("%v", key), "A") && !strings.HasPrefix(fmt.Sprintf("%v", key), "a") {
            continue A
        }
        if !strings.HasPrefix(fmt.Sprintf("%v", val), "A") && !strings.HasPrefix(fmt.Sprintf("%v", val), "a") {
            continue A
        }
    }
    return true
}

func CheckDictCase(dict map[interface{}]interface{}) bool {
    if len(dict) == 0 {
        return false
    }

    upper, lower := false, false

    for _, val := range dict {
        if strings.HasPrefix(fmt.Sprintf("%v", val), "A") || strings.HasPrefix(fmt.Sprintf("%v", val), "a") {
            lower = true
        } else if strings.HasPrefix(fmt.Sprintf("%v", val), "A") || strings.HasPrefix(fmt.Sprintf("%v", val), "a") {
            upper = true
        } else {
            return false
        }
    }
    return upper || lower
}

// CheckDictCase(map[interface{}]interface{}{"a":"apple", "b":"banana"})
// CheckDictCase(map[interface{}]interface{}{"a":"apple", "A":"banana", "B":"banana"})
// CheckDictCase(map[interface{}]interface{}{"a":"apple", 8:"banana", "a":"apple"})
// CheckDictCase(map[interface{}]interface{}{"Name":"John", "Age":"36", "City":"Houston"})
// CheckDictCase(map[interface{}]interface{}{"STATE":"NC", "ZIP":"12345" })
