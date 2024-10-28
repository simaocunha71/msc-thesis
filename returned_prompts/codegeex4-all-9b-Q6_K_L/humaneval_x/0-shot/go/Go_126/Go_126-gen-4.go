func IsSorted(lst []int) bool {
    // This is the solution for the problem. It iterates through the list of numbers and checks if the current number is greater than the next one. If it is, it returns false. If it iterates through the entire list without finding a number that is greater than the next one, it returns true.
    for i := 0; i < len(lst)-1; i++ {
        if lst[i] > lst[i+1] {
            return false
        }
    }
    return true
}