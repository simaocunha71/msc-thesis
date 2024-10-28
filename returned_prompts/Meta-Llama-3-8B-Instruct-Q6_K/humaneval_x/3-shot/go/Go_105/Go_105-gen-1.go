    sort.Slice(arr, func(i, j int) bool {
        return arr[i] < arr[j]
    })
    result := make([]string, 0)
    for _, num := range arr {
        if num < 10 && num > 0 {
            switch num {
            case 1:
                result = append(result, "One")
            case 2:
                result = append(result, "Two")
            case 3:
                result = append(result, "Three")
            case 4:
                result = append(result, "Four")
            case 5:
                result = append(result, "Five")
            case 6:
                result = append(result, "Six")
            case 7:
                result = append(result, "Seven")
            case 8:
                result = append(result, "Eight")
            case 9:
                result = append(result, "Nine")
            }
        }
    }
    reverse(result)
    return result
}

func reverse(a []string) {
    for i, j := 0, len(a)-1; i < j; i, j = i+1, j-1 {
        a[i], a[j] = a[j], a[i]
    }
}