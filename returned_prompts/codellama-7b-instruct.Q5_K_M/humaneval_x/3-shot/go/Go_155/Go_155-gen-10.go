    even_digits := 0
    odd_digits := 0
    for _, digit := range strconv.Itoa(num) {
        if digit == "0" {
            even_digits += 1
        } else if digit == "1" {
            odd_digits += 1
        } else if digit == "2" {
            even_digits += 1
        } else if digit == "3" {
            odd_digits += 1
        } else if digit == "4" {
            even_digits += 1
        } else if digit == "5" {
            odd_digits += 1
        } else if digit == "6" {
            even_digits += 1
        } else if digit == "7" {
            odd_digits += 1
        } else if digit == "8" {
            even_digits += 1
        } else if digit == "9" {
            odd_digits += 1
        }
    }
    return [2]int{even_digits, odd_digits}
}



