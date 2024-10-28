    var minEven int = math.MaxInt32
    var minIndex int = -1
    for i, num := range arr {
        if num % 2 == 0 && num < minEven {
            minEven = num
            minIndex = i
        }
    }
    if minIndex == -1 {
        return []int{}
    }
    return []int{minEven, minIndex}
} 