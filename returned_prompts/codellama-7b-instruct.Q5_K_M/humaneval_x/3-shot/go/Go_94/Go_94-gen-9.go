    var largest_prime int

    for _, number := range lst {
        if number > largest_prime {
            if IsPrime(number) {
                largest_prime = number
            }
        }
    }

    return SumDigits(strconv.Itoa(largest_prime))
}



