```go
func CheckDictCase(dict map[interface{}]interface{}) bool {
    if len(dict) == 0 {
        return false
    }

    allLower := true
    allUpper := true

    for k := range dict {
        if s, ok := k.(string); ok {
            if !strings.ToLower(s) == s {
                allLower = false
            }
            if !strings.ToUpper(s) == s {
                allUpper = false
            }
        } else {
            return false
        }
    }

    return allLower || allUpper
}
```
