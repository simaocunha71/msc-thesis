    if len(dict) == 0 {
        return false
    }

    var case_type string = ""
    for k, _ := range dict {
        if _, ok := k.(string); !ok {
            return false
        }
        if case_type != "" && case_type != strings.ToLower(k.(string)) && case_type != strings.ToUpper(k.(string)) {
            return false
        }
        case_type = strings.ToLower(k.(string))
    }
    return true
}



