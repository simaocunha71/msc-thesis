    sort.Ints(arr)
    var newArr []string
    for i := len(arr) - 1; i >= 0; i-- {
        if arr[i] >= 1 && arr[i] <= 9 {
            switch arr[i] {
            case 1:
                newArr = append(newArr, "One")
            case 2:
                newArr = append(newArr, "Two")
            case 3:
                newArr = append(newArr, "Three")
            case 4:
                newArr = append(newArr, "Four")
            case 5:
                newArr = append(newArr, "Five")
            case 6:
                newArr = append(newArr, "Six")
            case 7:
                newArr = append(newArr, "Seven")
            case 8:
                newArr = append(newArr, "Eight