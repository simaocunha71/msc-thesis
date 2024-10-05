    result := make([]string, 0)

    for _, c := range text {
        if c == ' ' {
            result = append(result, "_")
        }else{
            result = append(result, string(c))
        }
    }

    for i := 0; i < len(result)-1; i++ {
        if result[i] == "_" && result[i+1] == "_" {
            result[i+1] = "-"
        }
    }
    return strings.Join(result, "")
}



