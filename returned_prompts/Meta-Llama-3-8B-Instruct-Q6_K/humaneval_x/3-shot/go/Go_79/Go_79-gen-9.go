    binary := ""
    for decimal > 0 {
        remainder := decimal % 2
        if remainder == 0 {
            binary = "0" + binary
        } else {
            binary = "1" + binary
        }
        decimal = decimal / 2
    }
    return "db" + binary + "db"
}