    for i := 0; i < len(arr); i++ {
        if i == len(arr)-1 {
            //fmt.Println("i is at last index", i)
            break A
        }
        if arr[i] > arr[i+1] {
            //fmt.Println("i is less than i+1")
            return false
        }
    }
    return true
}
