    start = max(interval1[0], interval2[0])
    end   = min(interval1[1], interval2[1])

    if start > end {
        return "NO"
    }

    length := end - start + 1
    if length < 2 {
        return "NO"
    }

    isPrime := true
    for i := 2; i * i <= length; i++ {
        if length % i == 0 {
            isPrime = false
            break
        }
    }
    if isPrime {
        return "YES"
    } else {
        return "NO"
    }
}