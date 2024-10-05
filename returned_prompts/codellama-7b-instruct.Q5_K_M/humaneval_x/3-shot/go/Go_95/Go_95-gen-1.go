    if len(dict) == 0 {
        return false
    }

    var lower_case_flag bool
    for key, _ := range dict {
        str_key := strings.ToLower(fmt.Sprint(key))
        if lower_case_flag == false {
            if str_key == strings.ToLower(fmt.Sprint(key)) {
                lower_case_flag = true
            } else {
                return false
            }
        }
    }
    return true
}



