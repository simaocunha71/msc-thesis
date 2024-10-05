    prime_digits := map[rune]bool{
        '2': true, '3': true, '5': true, '7': true, 'B': true, 'D': true,
    }

    result := 0
    for _, digit := range num {
        if prime_digits[digit] {
            result++
        }
    }
    return result
}



