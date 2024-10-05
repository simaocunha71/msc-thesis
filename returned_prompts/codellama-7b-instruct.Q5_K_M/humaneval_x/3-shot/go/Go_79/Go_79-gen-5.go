    var binary_number string
    for i := 0; i < 8; i++{
        binary_number = "db" + string(decimal%2) + binary_number
        decimal /= 2
    }
    return binary_number
}



