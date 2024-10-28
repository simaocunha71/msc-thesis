    var sum_of_squares int = 0
    var sum_of_odd_numbers int = 0

    for _, number := range lst {
        if number >= 0 && int(number) == number {
            sum_of_odd_numbers += number
            sum_of_squares += int(math.Pow(number, 2))
        }
    }

    return 2 * (sum_of_squares - sum_of_odd_numbers)
}



