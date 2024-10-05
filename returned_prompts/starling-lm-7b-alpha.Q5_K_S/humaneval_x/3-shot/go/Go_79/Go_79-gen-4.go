    result := make([]byte, 0)
    for decimal > 0 {
        result = append(result, byte(decimal % 2 + '0'))
        decimal /= 2
    }
    return "db" + string(result) + "db"
}



