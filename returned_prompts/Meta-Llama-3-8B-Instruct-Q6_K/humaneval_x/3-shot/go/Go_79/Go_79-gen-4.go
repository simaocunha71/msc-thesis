    binary := fmt.Sprintf("db")
    for decimal > 0 {
        remainder := decimal % 2
        if remainder == 1 {
            binary = fmt.Sprintf("%s1", binary)
        } else {
            binary = fmt.Sprintf("%s0", binary)
        }
        decimal = decimal / 2
    }
    binary = fmt.Sprintf("%sb", binary)
    return binary
}