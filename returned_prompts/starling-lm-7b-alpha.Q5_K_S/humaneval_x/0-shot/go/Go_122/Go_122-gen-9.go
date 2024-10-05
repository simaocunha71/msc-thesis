    sum := 0
    for i := 0; i < k; i++ {
        s := strconv.Itoa(arr[i])
        if len(s) <= 2 {
            sum += arr[i]
        }
    }
    return sum

}


func AddElements(arr []int, k int) int {
    sum := 0
    for i := 0; i < k; i++ {
        if len(strconv.Itoa(arr[i])) <= 2 {
            sum += arr[i]
        }
    }
    return sum
}


func AddElements(arr []int, k int) int {
    sum := 0
    for _, v := range arr[:k] {
        if len(strconv.Itoa(v)) <= 2 {
            sum += v
        }
    }
    return sum
}


func AddElements(arr []int, k int) int {
    sum := 0
    for i := 0; i < k; i++ {
        if len(strconv.Itoa(arr[i])) <= 2 {
            sum += arr[i]
        }
    }
    return sum
}


func AddElements(arr []int, k int) int {
    sum := 0
    for i := 0; i < k; i++ {
        if len(strconv.Itoa(arr[i])) <= 2 {
            sum += arr[i]
        }
    }
    return sum
}


func AddElements(arr []int, k int) int {
    sum := 0
    for i := 0; i < k; i++ {
        if len(strconv.Itoa(arr[i])) <= 2 {
            sum += arr[i]
        }
    }
    return sum
}


func AddElements(arr []int, k int) int {
    sum := 0
    for _, v := range arr[:k] {
        if len(strconv.Itoa(v)) <= 2 {
            sum += v
        }
    }
    return sum
