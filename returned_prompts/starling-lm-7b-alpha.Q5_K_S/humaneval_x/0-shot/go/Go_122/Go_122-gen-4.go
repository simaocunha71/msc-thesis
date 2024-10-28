    sum := 0
    for i := 0; i < k && i < len(arr); i++ {
        sum += arr[i]
    }
    return sum
}

    // return sum of all elements with at most two digits
    sum := 0
    for _, val := range arr {
        if len(strconv.Itoa(val)) <= 2 {
            sum += val
        }
    }
    return sum
}

    // return sum of all elements with at most two digits
    sum := 0
    for i := range arr[:k] {
        if len(strconv.Itoa(arr[i])) <= 2 {
            sum += arr[i]
        }
    }
    return sum
}

    // return sum of all elements with at most two digits
    sum := 0
    for i := range arr[:k] {
        if len(strconv.Itoa(arr[i])) <= 2 {
            sum += arr[i]
        }
    }
    return sum
}

*/
































































































































































































































































