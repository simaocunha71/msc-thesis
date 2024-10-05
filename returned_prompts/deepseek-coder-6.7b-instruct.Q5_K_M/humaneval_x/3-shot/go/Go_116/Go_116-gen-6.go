    sort.Slice(arr, func(i, j int) bool {
        return fmt.Sprintf("%b",arr[i]) < fmt.Sprintf("%b",arr[j])
    })
    return arr
}



