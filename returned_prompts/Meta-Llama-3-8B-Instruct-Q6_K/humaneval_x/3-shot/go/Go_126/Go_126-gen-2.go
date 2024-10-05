    if len(lst) <= 1 {
        return true
    }
    for i := 1; i < len(lst); i++ {
        if lst[i] <= lst[i-1] {
            return false
        }
    }
    return true
}  // Note: This function does not handle duplicate elements. If you want to handle duplicate elements, you can add a check inside the for loop. For example: if lst[i] <= lst[i-1] && lst[i] != lst[i-1] { return false }