    binary := ""
    for decimal > 0 {
        remainder := decimal % 2
        decimal = decimal / 2
        if remainder == 1 {
            binary = "1" + binary
        } else {
            binary = "0" + binary
        }
    }
    return "db" + binary + "db"
}