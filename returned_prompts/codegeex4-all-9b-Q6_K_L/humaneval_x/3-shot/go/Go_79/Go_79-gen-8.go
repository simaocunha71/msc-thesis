    binary := ""
    for decimal > 0 {
        remainder := decimal % 2
        binary = string(remainder) + binary
        decimal /= 2
    }
    return "db" + binary + "db"
}

