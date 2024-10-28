    var fibSeq []int
    var i int = 0
    var j int = 1

    for len(fibSeq) < n {
        fibSeq = append(fibSeq, i)
        i, j = j, i+j
    }

    var primeFibs []int
    for _, fibNum := range fibSeq {
        if IsPrime(fibNum) {
            primeFibs = append(primeFibs, fibNum)
        }
    }

    return primeFibs[n-1]
}

func IsPrime(n int) bool {
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


