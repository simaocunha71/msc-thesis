    var countEven, countOdd int = 0, 0
    numStr := strconv.Itoa(num)
    for _, char := range numStr {
        if char == '0' || char == '2' || char == '4' || char == '6' || char == '8' {
            countEven++
        } else if char == '1' || char == '3' || char == '5' || char == '7' || char == '9' {
            countOdd++
        }
    }
    return [2]int{countEven, countOdd}
}



