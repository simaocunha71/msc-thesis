    var xNum, xDen, nNum, nDen int
    var isSimplified bool = true
    if strings.Index(x, "/") != -1 {
        xNum, _ = strconv.Atoi(strings.Split(x, "/")[0])
        xDen, _ = strconv.Atoi(strings.Split(x, "/")[1])
    } else {
        xNum = x Den = 1
    }
    if strings.Index(n, "/") != -1 {
        nNum, _ = strconv.Atoi(strings.Split(n, "/")[0])
        nDen, _ = strconv.Atoi(strings.Split(n, "/")[1])
    } else {
        nNum = n Den = 1
    }
    if nNum*xDen != nDen*xNum {
        isSimplified = false
    }
    if isSimplified {
        g := gcd(nNum*xDen, nDen*xNum)
        nNum = nNum*xDen / g
        nDen = nDen*xNum / g
    }
    if nNum*xDen != nDen*xNum {
        isSimplified = false
    }
    return isSimplified
}

func gcd(a, b int) int {
    for b > 0 {
        a, b = b, a%b
    }
    return a
}

func simplify(x, n string) bool {
    xNum, xDen := 0, 0
    nNum, nDen := 0, 0
    if strings.Index(x, "/") != -1 {
        xNum, _ = strconv.Atoi(strings.Split(x, "/")[0])
        xDen, _ = strconv.Atoi(strings.Split(x, "/")[1])
    } else {
        xNum = x
        xDen = 1
    }
    if strings.Index(n, "/") != -1 {
        nNum, _ = strconv.Atoi(strings.Split(n, "/")[0])
