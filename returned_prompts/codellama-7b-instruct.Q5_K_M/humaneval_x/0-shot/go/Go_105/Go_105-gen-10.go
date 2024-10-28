    for _, v := range arr {
        if v < 1 || v > 9 {
            goto A
        }
    }
    sort.Ints(arr)
    arr = reverse(arr)
    for i, v := range arr {
        arr[i] = name[v-1]
    }
    return arr
}

func reverse(arr []int)[]int {
    for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
        arr[i], arr[j] = arr[j], arr[i]
    }
    return arr
}
