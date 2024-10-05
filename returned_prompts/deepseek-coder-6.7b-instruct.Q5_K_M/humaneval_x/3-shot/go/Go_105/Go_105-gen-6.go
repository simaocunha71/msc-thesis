    if len(arr)==0{
        return []string{}
    }
    sort.Ints(arr)
    for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
        arr[i], arr[j] = arr[j], arr[i]
    }
    result := make([]string, len(arr))
    for i, v := range arr {
        if v>=1 && v<=9 {
            switch v {
            case 1:
                result[i] = "One"
            case 2:
                result[i] = "Two"
            case 3:
                result[i] = "Three"
            case 4:
                result[i] = "Four"
            case 5:
                result[i] = "Five"
            case 6:
                result[i] = "Six"
            case 7:
                result[i] = "Seven"
            case 8:
                result[i] = "Eight"
            case 9:
                result[i] = "Nine"
            }
        }
    }
    return result
}



