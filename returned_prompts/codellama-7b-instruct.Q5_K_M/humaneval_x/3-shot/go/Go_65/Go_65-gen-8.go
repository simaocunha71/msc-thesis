    result := make([]byte, 0)
    x_str := fmt.Sprintf("%d", x)
    for i := 0; i < len(x_str); i++ {
        result = append(result, x_str[i+shift])
    }
    return string(result)
}




