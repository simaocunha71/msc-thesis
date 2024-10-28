    for i, j := 0, 0; i < len(arr); i++ {
        if arr[i]%2 == 0 {
            j = i
            break A
        }
    }
    if j == 0 {
        return []int{}
    }
    for i := j + 1; i < len(arr); i++ {
        if arr[i]%2 == 0 && arr[i] < arr[j] {
            j = i
        }
    }
    return []int{arr[j], j}
}

func Pluck2(arr []int) []int {
    min := math.MaxInt32
    var index int
    for i, v := range arr {
        if v%2 == 0 && v < min {
            min = v
            index = i
        }
    }
    if index == 0 {
        return []int{}
    }
    return []int{min, index}
}

func Pluck3(arr []int) []int {
    min := math.MaxInt32
    var index int
    for i, v := range arr {
        if v%2 == 0 && v < min {
            min = v
            index = i
        }
    }
    if min == math.MaxInt32 {
        return []int{}
    }
    return []int{min, index}
}
