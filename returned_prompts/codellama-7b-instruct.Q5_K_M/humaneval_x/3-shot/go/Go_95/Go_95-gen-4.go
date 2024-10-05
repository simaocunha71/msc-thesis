    if len(dict) == 0{
        return false
    }

    key_type := reflect.TypeOf(dict[0]).Kind()
    if key_type == reflect.String {
        for k,v := range dict {
            if reflect.TypeOf(k).Kind() == reflect.String {
                if strings.ToLower(k.(string)) != k.(string) {
                    return false
                }
                if reflect.TypeOf(v).Kind() == reflect.String {
                    if strings.ToLower(v.(string)) != v.(string) {
                        return false
                    }
                }
            }else{
                return false
            }
        }
        return true
    }else{
        return false
    }
}



