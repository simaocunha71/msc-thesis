    if len(dict) == 0 {
        return false
    }
    for _, key := range dict {
        if _, ok := key.(string); !ok {
            return false
        }
        if strings.ToLower(string(key)) != string(key) {
            for _, k := range dict {
                if strings.ToUpper(string(k)) != string(k) {
                    return false
                }
            }
            return true
        }
    }
    return true
}  // or simply return strings.ToLower(string(key)) == string(key) for all keys  // or return strings.ToUpper(string(key)) == string(key) for all keys}  // or return strings.ToLower(string(key)) == string(key) for all keys}  // or return strings.ToUpper(string(key)) == string(key) for all keys}  // or return strings.ToLower(string(key)) == string(key) for all keys}  // or return strings.ToUpper(string(key)) == string(key) for all keys}  // or return strings.ToLower(string(key)) == string(key) for all keys}  // or return strings.ToUpper(string(key)) == string(key) for all keys}  // or return strings.ToLower(string(key)) == string(key) for all keys}  // or return strings.ToUpper(string(key)) == string(key) for all keys}  // or return strings.ToLower(string(key)) == string(key) for all keys}  // or return strings.ToUpper(string(key)) == string(key) for all keys}  // or return strings.ToLower(string(key)) == string(key) for all keys}  // or return strings.ToUpper(string(key)) == string(key) for all keys}  // or return strings.ToLower(string(key)) == string(key) for all keys}  // or return strings.ToUpper(string(key)) == string(key) for all keys}  // or return strings.ToLower(string(key)) == string(key) for all keys}  // or return strings.ToUpper(string(key)) == string(key) for all keys}  // or return strings.ToLower(string(key)) == string(key) for all keys}  // or return strings.ToUpper(string(key)) == string(key) for all keys}  // or return strings.ToLower(string(key)) == string(key) for all keys}  // or return strings.ToUpper(string(key)) == string(key) for all keys}  // or return strings.ToLower(string(key)) == string(key) for all keys}  // or return strings.ToUpper(string(key)) == string(key) for all keys}  // or return strings.ToLower(string(key)) ==