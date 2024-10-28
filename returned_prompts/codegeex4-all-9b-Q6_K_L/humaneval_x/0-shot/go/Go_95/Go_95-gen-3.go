```go
func CheckDictCase(dict map[interface{}]interface{}) bool {
    if len(dict) == 0 {
        return false
    }
    isLower := true
    isUpper := true
    for key := range dict {
        if keyStr, ok := key.(string); ok {
            if strings.ToLower(keyStr) != keyStr {
                isLower = false
            }
            if strings.ToUpper(keyStr) != keyStr {
                isUpper = false
            }
        } else {
            return false
        }
    }
    return isLower || isUpper
}
```
