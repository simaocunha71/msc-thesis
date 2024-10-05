    binary := ""
    for decimal > 0 {
        binary = fmt.Sprintf("%d%s", decimal%2, binary)
        decimal /= 2
    }
    return "db" + binary + "db"
}



