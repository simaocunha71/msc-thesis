    if decimal==0{
        return "db0db"
    }

    var binary string = "db"
    for decimal>0{
        binary = string(decimal%2) + binary
        decimal = decimal/2
    }
    binary = binary + "db"
    return binary
}



