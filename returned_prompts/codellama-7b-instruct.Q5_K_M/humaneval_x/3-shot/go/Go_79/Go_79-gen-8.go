    var result string
    if decimal == 0 {
        result = "db0db"
    } else {
        for decimal > 0 {
            if decimal%2 == 0 {
                result = "0" + result
            } else {
                result = "1" + result
            }
            decimal = decimal/2
        }
        result = "db" + result + "db"
    }
    return result
}



