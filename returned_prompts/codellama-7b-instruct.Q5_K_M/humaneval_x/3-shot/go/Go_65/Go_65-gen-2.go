    result := make([]rune, 0)
    var num_digits int = 0

    for x > 0 {
        num_digits += 1
        x /= 10
    }

    if shift > num_digits {
        shift = num_digits
    }

    for i := 1; i <= num_digits; i++ {
        result = append(result, rune(int('0' + x%10)))
        x /= 10
    }

    return string(result[shift:]) + string(result[:shift])
}



