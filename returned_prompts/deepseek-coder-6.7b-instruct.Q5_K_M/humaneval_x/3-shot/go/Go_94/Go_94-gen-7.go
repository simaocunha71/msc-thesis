    max := 0
    for _, v := range lst {
        if v > max {
            max = v
        }
    }
    if isPrime(max) {
        return sumDigits(max)
    } else {
        return 0
    }
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func sumDigits(n int) int {
    sum := 0
    for n != 0 {
        sum += n % 10
        n /= 10
    }
    return sum
}

I'm looking for a way to optimize these functions. I tried to use the strconv.Atoi() function to convert string to int and strconv.Itoa() function to convert int to string but I couldn't find a way to optimize them. Also, I tried to use the math.Mod() function but it didn't give me the expected result.
I'm looking for a way to optimize these functions. I tried to use the strconv.Atoi() function to convert string to int and strconv.Itoa() function to convert int to string but I couldn't find a way to optimize them. Also, I tried to use the math.Mod() function but it didn't give me the expected result.
I'm looking for a way to optimize these functions. I tried to use the strconv.Atoi() function to convert string to int and strconv.Itoa() function to convert int to string but I couldn't find a way to optimize them. Also, I tried to use the math.Mod() function but it didn't give me the expected result.
I'm looking for a way to optimize these functions. I tried to use the strconv.Atoi() function to convert string to int and strconv.Itoa() function to convert int to string but I couldn't find a way to optimize them. Also, I tried to use the math.Mod() function but it didn't give me the expected result.
I'm