```go
func CheckDictCase(dict map[interface{}]interface{}) bool {
    if len(dict) == 0 {
        return false
    }
    lower := true
    upper := true
    for k := range dict {
        if _, ok := k.(string); !ok {
            return false
        }
        if strings.ToLower(k.(string)) != k.(string) {
            lower = false
        }
        if strings.ToUpper(k.(string)) != k.(string) {
            upper = false
        }
        if !lower && !upper {
            return false
        }
    }
    return lower || upper
}
```
