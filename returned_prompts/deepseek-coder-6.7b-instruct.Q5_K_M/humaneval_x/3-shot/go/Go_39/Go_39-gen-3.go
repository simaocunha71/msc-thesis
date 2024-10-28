    var fibSeq []int
    var i = 0
    var j = 1
    var fibNum = 0
    var primeNum = 0

    for {
        fibNum = i + j
        i = j
        j = fibNum
        if IsPrime(fibNum) {
            primeNum++
            if primeNum == n {
                return fibNum
            }
        }
    }
    return 0
}

func IsPrime(n int) bool {
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
    for i*i <= n {
        if n%i == 0 || n%(i+2) == 0 {
            return false
        }
        i += 6
    }
    return true
}


