    largest_prime := 0
    for _, number := range lst {
        if number > largest_prime{
            largest_prime = number
        }
    }

    var sum int
    for _, digit := range strconv.Itoa(largest_prime){
        sum += int(digit - '0')
    }
    return sum
}



