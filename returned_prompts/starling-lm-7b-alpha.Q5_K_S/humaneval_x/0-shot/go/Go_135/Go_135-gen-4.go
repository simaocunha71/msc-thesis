
func CanArrange(arr []int) int {
    index := 0
    for i := 0; i < len(arr)-1; i++ {
        if arr[index] < arr[i] {
            index = i
        }
    }
    if index == len(arr)-1 {
        return index
    }
    for i := index + 1; i < len(arr); i++ {
        if arr[i] <= arr[i-1] {
            return i
        }
    }
    return -1
}

    index := 0
    for i := 0; i < len(arr)-1; i++ {
        if arr[index] < arr[i] {
            index = i
        }
    }
    if index == len(arr)-1 {
        return index
    }
    for i := index + 1; i < len(arr); i++ {
        if arr[i] <= arr[i-1] {
            return i
        }
    }
    return -1
}






































































































































































































































































