    max := 0
    for _, v := range lst {
        if v > max {
            max = v
        }
    }
    prime := isprime(max)
    if !prime {
        return 0
    }
    sum := 0
    for _, v := range strconv.Itoa(max) {
        sum += int(v - 48)
    }
    return sum
}

func isprime(n int) bool {
    if n <= 1 {
        return false
    }
    if n <= 3 {
        return true
    }
    if n%2 == 0 || n%3 == 0 {
        return false
    }
    i := 5
    for i * i <= n {
        if n%i == 0 || n%(i + 2) == 0 {
            return false
        }
        i += 6
    }
    return true
}

/*
You are given a list of integers.
You need to find the largest prime value and return the sum of its digits.

Examples:
For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
For lst = [0