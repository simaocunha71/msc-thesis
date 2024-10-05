    var result_string string = ""
    for _, s_char := range s {
        if !strings.Contains(c,string(s_char)){
            result_string += string(s_char)
        }
    }
    if strings.Contains(result_string,string(result_string[len(result_string)-1])+string(result_string[len(result_string)-1])){
        return [2]interface{}{result_string, true}
    }
    return [2]interface{}{result_string, false}
}



