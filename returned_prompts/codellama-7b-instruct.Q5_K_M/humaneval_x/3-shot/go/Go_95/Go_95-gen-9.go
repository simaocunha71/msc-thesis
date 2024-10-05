    if len(dict) == 0 {
        return true
    }
    lower_case := false
    for key, _ := range dict {
        if lower_case == false {
            lower_case = strings.ToLower(key.(string)) == key.(string)
        } else {
            if lower_case != strings.ToLower(key.(string)) == key.(string) {
                return false
            }
        }
    }
    return true
}



