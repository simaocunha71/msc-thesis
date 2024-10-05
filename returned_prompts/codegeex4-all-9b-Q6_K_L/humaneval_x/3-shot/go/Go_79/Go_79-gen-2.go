    binary := ""
    for decimal > 0 {
        binary = string(decimal%2) + binary
        decimal = decimal / 2
    }
    return "db" + binary + "db"
}

