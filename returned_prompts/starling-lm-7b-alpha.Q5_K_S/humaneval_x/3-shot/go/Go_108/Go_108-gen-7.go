    result := 0
    for _, n := range arr {
        if IsPositiveSumOfDigits(n) {
            result += 1
        }
    }
    return result
}



