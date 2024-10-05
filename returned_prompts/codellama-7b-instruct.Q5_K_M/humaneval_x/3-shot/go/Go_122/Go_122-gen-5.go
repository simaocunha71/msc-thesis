    var sum int
    if k > len(arr) {
        k = len(arr)
    }

    for i := 0; i < k; i++ {
        str_arr := strconv.Itoa(arr[i])
        if len(str_arr) > 2 {
            continue
        }
        sum += arr[i]
    }
    return sum
}



