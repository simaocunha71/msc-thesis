    result := make([]string, 0)

    for _, c := range text {
        if c == ' ' {
            result = append(result, "_")
        }else{
            result = append(result, string(c))
        }
    }
    return strings.Join(result, "")
}



