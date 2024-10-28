    result := 0

    // check if array is already palindromic
    if arr == ReverseArray(arr){
        return result
    }

    // if not, find the smallest difference between two elements
    for i := 0; i < len(arr)-1; i++ {
        for j := i+1; j < len(arr); j++ {
            if arr[i] != arr[j] {
                if result == 0 {
                    result = math.Abs(arr[i] - arr[j])
                } else {
                    result = int(math.Min(float64(result), math.Abs(arr[i] - arr[j])))
                }
            }
        }
    }
    return result
}



