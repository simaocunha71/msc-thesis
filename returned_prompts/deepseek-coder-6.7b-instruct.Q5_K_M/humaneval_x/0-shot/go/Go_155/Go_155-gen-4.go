    var countEven int
    var countOdd int
    numStr := strconv.Itoa(num)
    for _, v := range numStr {
        numInt, _ := strconv.Atoi(string(v))
        if numInt%2 == 0 {
            countEven++
        } else {
            countOdd++
        }
    }
    return 배열[2]int{countEven, countOdd}
}


