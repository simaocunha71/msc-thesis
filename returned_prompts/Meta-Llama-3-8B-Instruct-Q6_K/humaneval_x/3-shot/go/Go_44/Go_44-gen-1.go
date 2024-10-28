    var result string
    var remainder int
    var temp int

    for x > 0 {
        temp = x % base
        if temp >= 10 {
            result = string(rune(65 + temp - 10)) + result  // Convert to uppercase letter if temp is greater than 9
        } else {
            result = strconv.Itoa(temp) + result
        }
        x = x / base
    }
    return result
}