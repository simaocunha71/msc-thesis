    roman := ""
    num := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
    sym := []string{"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"}

    for i := 0; i < len(num); i++ {
        for number >= num[i] {
            roman += sym[i]
            number -= num[i]
        }
    }

    return strings.ToLower(roman)
}

