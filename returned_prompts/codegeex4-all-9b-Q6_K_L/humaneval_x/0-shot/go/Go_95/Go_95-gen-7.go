```go
func CheckDictCase(dict map[interface{}]interface{}) bool {
    if len(dict) == 0 {
        return false
    }

    firstKey := ""
    for k := range dict {
        if s, ok := k.(string); ok {
            firstKey = s
            break
        }
    }
    if firstKey == "" {
        return false
    }

    allLower := strings.ToLower(firstKey) == firstKey
    allUpper := strings.ToUpper(firstKey) == firstKey

    for k := range dict {
        if s, ok := k.(string); ok {
            if allLower && strings.ToLower(s) != s {
                return false
            }
            if allUpper && strings.ToUpper(s) != s {
                return false
            }
        } else {
            return false
        }
    }
    return true
}
```
