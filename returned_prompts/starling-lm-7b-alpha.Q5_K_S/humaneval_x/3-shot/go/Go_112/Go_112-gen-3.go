    result := strings.ReplaceAll(s, c[0], "")
    result = strings.ReplaceAll(result, c[1], "")
    if result == strings.Join(strings.Split(result, "")[::-1], "") {
        return [2]interface{}{result, true}
    } else {
        return [2]interface{}{result, false}
    }
}



