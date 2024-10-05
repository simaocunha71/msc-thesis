```go
func CheckDictCase(dict map[interface{}]interface{}) bool {
    if len(dict) == 0 {
        return false
    }

    firstKey := true
    upper := false
    lower := false

    for key := range dict {
        if firstKey {
            if _, ok := key.(string); !ok {
                return false
            }
            if strings.ToUpper(key.(string)) == key.(string) {
                upper = true
            } else if strings.ToLower(key.(string)) == key.(string) {
                lower = true
            } else {
                return false
            }
            firstKey = false
        } else {
            if _, ok := key.(string); !ok {
                return false
            }
            if upper {
                if strings.ToUpper(key.(string)) != key.(string) {
                    return false
                }
            } else if lower {
                if strings.ToLower(key.(string)) != key.(string) {
                    return false
                }
            } else {
                return false
            }
        }
    }
    return upper || lower
}
```
