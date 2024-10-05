    sort.Ints(arr)

B:
    for i, v := range arr {
        if v < 1 || v > 9 {
            arr = append(arr[:i], arr[i+1:]...)
            goto A
        }
    }

C:
    arr = append(arr, arr[:0]...)

D:
    for _, v := range arr {
        switch v {
        case 1:
            arr[i] = "One"
        case 2:
            arr[i] = "Two"
        case 3:
            arr[i] = "Three"
        case 4:
            arr[i] = "Four"
        case 5:
            arr[i] = "Five"
        case 6:
            arr[i] = "Six"
        case 7:
            arr[i] = "Seven"
        case 8:
            arr[i] = "Eight"
        case 9:
            arr[i] = "Nine"
        }
        i++
    }

    return arr
}
