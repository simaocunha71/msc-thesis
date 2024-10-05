    result := []rune{}
    for _, c1 := range s {
        if !strings.Contains(c, string(c1)) {
            result = append(result, c1)
        }
    }
    result_str := string(result)
    if strings.EqualFold(result_str, strings.Reverse(result_str)) {
        return [2]interface{}{result_str, true}
    } else {
        return [2]interface{}{result_str, false}
    }
}