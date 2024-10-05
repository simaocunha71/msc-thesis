    var prime_digits = make(map[string]bool)
    prime_digits["2"] = true
    prime_digits["3"] = true
    prime_digits["5"] = true
    prime_digits["7"] = true
    prime_digits["B"] = true
    prime_digits["D"] = true

    var digit_count = 0

    for _, c := range num {
        if _, ok := prime_digits[string(c)]; ok{
            digit_count += 1
        }
    }

    return digit_count
}



