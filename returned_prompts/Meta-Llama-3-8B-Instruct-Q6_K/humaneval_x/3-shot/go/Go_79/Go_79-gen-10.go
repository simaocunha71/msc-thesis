    binary := ""
    for decimal > 0 {
        remainder := decimal % 2
        decimal = decimal / 2
        binary = fmt.Sprintf("%d%s", remainder, binary)
    }
    return "db" + binary + "db"
}