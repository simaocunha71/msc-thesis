    result := make([]string, 0)

    for i, c := range a {
        if string(c) == string(b[i]) {
            result = append(result, "0")
        } else {
            result = append(result, "1")
        }
    }
    return fmt.Sprintf("%s", result)
}



