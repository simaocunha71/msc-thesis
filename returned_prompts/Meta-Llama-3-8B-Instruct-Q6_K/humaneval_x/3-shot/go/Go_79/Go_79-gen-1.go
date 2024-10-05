    result := "db"
    for decimal > 0 {
        remainder := decimal % 2
        if remainder == 1 {
            result = string('1') + result
        } else {
            result = string('0') + result
        }
        decimal = decimal / 2
    }
    result = result + "db"
    return result
} 



