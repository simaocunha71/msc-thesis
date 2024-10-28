    largestPrime := 0
    for _, v := range lst {
        if v > largestPrime {
            largestPrime = v
        }
    }
    s := strconv.Itoa(largestPrime)
    sum := 0
    for _, v := range s {
        sum += int(v - 48)
    }
    return sum
}



