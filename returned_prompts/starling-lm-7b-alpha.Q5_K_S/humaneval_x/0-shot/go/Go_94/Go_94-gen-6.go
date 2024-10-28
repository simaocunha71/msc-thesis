    // Convert the slice of integers to a slice of strings
    strs := make([]string, len(lst))
    for i := 0; i < len(lst); i++ {
        strs[i] = strconv.Itoa(lst[i])
    }

    // Find the maximum value in the slice of strings
    max := ""
    for _, str := range strs {
        if str > max {
            max = str
        }
    }

    // Convert the maximum value back to an integer
    maxInt, _ := strconv.Atoi(max)

    // Check if the maximum value is prime
    isPrime := true
    for i := 2; i <= int(math.Sqrt(float64(maxInt))); i++ {
        if maxInt%i == 0 {
            isPrime = false
            break
        }
    }

    // If the maximum value is not prime, increment it by one and check again
    if !isPrime {
        maxInt++
        for i := 2; i <= int(math.Sqrt(float64(maxInt))); i++ {
            if maxInt%i == 0 {
                isPrime = false
                break
            }
        }
    }

    // Sum the digits of the maximum value
    sum := 0
    for _, r := range strconv.Itoa(maxInt) {
        sum += int(r - '0')
    }

    return sum
}

func main() {
    fmt.Println(Skjkasdkd([]int{0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3})) // 10
    fmt.Println(Skjkasdkd([]int{1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2,