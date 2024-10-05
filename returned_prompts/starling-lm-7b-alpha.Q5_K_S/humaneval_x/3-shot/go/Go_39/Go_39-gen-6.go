    candidate := 2
    i := 3
    for n > 1 {
        candidate += i
        if CandidateIsPrime(candidate) && Fibonacci(candidate) == candidate {
            n--
        }
        i++
    }
    return candidate
}



