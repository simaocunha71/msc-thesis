    result := strings.ReplaceAll(s, c, "")
    if result == Reverse(result) {
        return [2]interface{}{result, true}
    } else {
        return [2]interface{}{result, false}
    }
}

func Reverse(s string) (result string) {
    for _, v := range s {
        result = string(v) + result
    }
    return
}

