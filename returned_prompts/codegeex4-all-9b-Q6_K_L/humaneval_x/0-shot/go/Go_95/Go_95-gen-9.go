```go
func CheckDictCase(dict map[interface{}]interface{}) bool {
    if len(dict) == 0 {
        return false
    }
    allLower := true
    allUpper := true
    for k := range dict {
        if v, ok := k.(string); ok {
            if strings.ToLower(v) != v {
                allUpper = false
            }
            if strings.ToUpper(v) != v {
                allLower = false
            }
        } else {
            return false
        }
    }
    return allLower || allUpper
}
```
