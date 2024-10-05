    for i := 0; i < len(arr); i++ {
        for j := i + 1; j < len(arr); j++ {
            if arr[i] > arr[j] {
                arr[i], arr[j] = arr[j], arr[i]
                goto A
            }
        }
    }
    return arr
}

func Sort(arr []int) []string {
    for i := 0; i < len(arr); i++ {
        arr[i] = arr[i] - 1
    }
    sort.Sort(sort.Reverse(sort.IntSlice(arr)))
    return arr
}

func Convert(arr []int) []string {
    names := [10]string{"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}
    for i := 0; i < len(arr); i++ {
        arr[i] = names[arr[i]]
    }
    return arr
}

func GetNames(arr []int) []string {
    arr = ByLength(arr)
    arr = Sort(arr)
    arr = Convert(arr)
    return arr
}
