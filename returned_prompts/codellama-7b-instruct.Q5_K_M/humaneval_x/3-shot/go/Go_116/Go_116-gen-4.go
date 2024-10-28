    var binary_string string
    var binary_arr []int
    var decimal_arr []int
    var result []int

    for i := 0; i < len(arr); i++ {
        binary_string = fmt.Sprintf("%b", arr[i])
        binary_arr = append(binary_arr, len(binary_string)-int(strings.Count(binary_string, "1")))
        decimal_arr = append(decimal_arr, arr[i])
    }

    sort.Slice(binary_arr, func(i, j int) bool {
        if binary_arr[i] == binary_arr[j] {
            return decimal_arr[i] < decimal_arr[j]
        }
        return binary_arr[i] < binary_arr[j]
    })

    for i := 0; i < len(binary_arr); i++ {
        result = append(result, decimal_arr[i])
    }
    return result
}



