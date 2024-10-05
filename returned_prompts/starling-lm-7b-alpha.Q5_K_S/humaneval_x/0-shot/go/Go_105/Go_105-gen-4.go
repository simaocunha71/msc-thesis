    arr = sort(arr)
    rev := reverse(arr)
    var s []string
    for _, v := range rev {
        switch v {
        case 1:
            s = append(s, "One")
        case 2:
            s = append(s, "Two")
        case 3:
            s = append(s, "Three")
        case 4:
            s = append(s, "Four")
        case 5:
            s = append(s, "Five")
        case 6:
            s = append(s, "Six")
        case 7:
            s = append(s, "Seven")
        case 8:
            s = append(s, "Eight")
        case 9:
            s = append(s, "Nine")
        }
    }
    return s
}

func reverse(arr []int) []int {
    for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
        arr[i], arr[j] = arr[j], arr[i]
    }
    return arr
}

func sort(arr []int) []int {
    sort.Ints(arr)
    return arr
}

ByLength([]int{2, 1, 1, 4, 5, 8, 2, 3}) // []string{"Two", "One", "One", "Four", "Five", "Eight", "Two", "Three"}
ByLength([]int{}) // []string{}
ByLength([]int{1, -1, 55}) // []string{"One"}



















































































































