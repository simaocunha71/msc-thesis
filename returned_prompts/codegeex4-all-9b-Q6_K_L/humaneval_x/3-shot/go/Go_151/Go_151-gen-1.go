    var sum int = 0
    for _, number := range lst {
        if number > 0 && number == math.Round(number) && number % 2 != 0 {
            sum += int(number * number)
        }
    }
    return sum
}



