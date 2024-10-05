    maxPrime := 0
    for _, num := range lst {
        isPrime := true
        if num < 2 {
            isPrime = false
        } else {
            for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
                if num%i == 0 {
                    isPrime = false
                    break
                }
            }
        }
        if isPrime && num > maxPrime {
            maxPrime = num
        }
    }
    sumDigits := 0
    for _, digit := range strconv.Itoa(maxPrime) {
        sumDigits += int(digit - '0')
    }
    return sumDigits
}