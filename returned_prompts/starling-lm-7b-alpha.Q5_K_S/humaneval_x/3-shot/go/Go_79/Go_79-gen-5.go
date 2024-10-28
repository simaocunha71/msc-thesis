    result := "db"

    for decimal > 0 {
        result += fmt.Sprintf("%d", decimal % 2)
        decimal /= 2
    }
    result += "db"

    return result
}



