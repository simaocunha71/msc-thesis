    result := make([]string, 0)

    for i := 0; i < len(a); i++ {
        if a[i] == '0' && b[i] == '0' {
            result = append(result, "0")
        }else if a[i] == '1' && b[i] == '1' {
            result = append(result, "0")
        }else if a[i] == '1' && b[i] == '0' {
            result = append(result, "1")
        }else if a[i] == '0' && b[i] == '1' {
            result = append(result, "1")
        }
    }
    return fmt.Sprintf("%s", result)
}



