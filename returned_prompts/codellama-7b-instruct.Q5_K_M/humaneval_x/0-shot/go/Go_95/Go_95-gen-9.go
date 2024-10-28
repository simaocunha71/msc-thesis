func CheckDictCase(dict map[interface{}]interface{}) bool {

    for k, v := range dict {
        str, ok := k.(string)
        if !ok {
            return false
        }
        if strings.ToLower(str) != str && strings.ToUpper(str) != str {
            return false
        }
        switch v.(type) {
        case string:
            if strings.ToLower(v.(string)) != v.(string) && strings.ToUpper(v.(string)) != v.(string) {
                return false
            }
        case map[interface{}]interface{}:
            if !CheckDictCase(v.(map[interface{}]interface{})) {
                return false
            }
        default:
            return false
        }
    }
    return true
}
