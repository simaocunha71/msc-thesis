    sort.Ints(l)
    for i := 0; i < len(l); i += 3 {
        l[i] = l[i+2]
        l[i+2] = l[i]
    }
    return l
}

I tried to run this code and it does not work. It says that the code has an error at l[i+2], "invalid operation: l[i+2] (mismatched types int and []int)"

A: Your function is almost correct but the operation l[i+2] is not valid because it's trying to access an integer value from an array, which is not the correct syntax.
The correct way to access the value from an array is to use the index like l[i] or l[i+2].
Instead of swapping l[i] and l[i+2], you should swap l[i+1] and l[i+2] if the length of array is divisible by three.
Here's the corrected code:
func SortThird(l []int) []int {
    sort.Ints(l)
    for i := 0; i < len(l); i += 3 {
        l[i+1], l[i+2] = l[i+2], l[i+1]
    }
    return l
}

This code first sorts the array. Then it swaps the value at l[i+1] with the value at l[i+2] in steps of three.

A: The error message is due to the fact that you're trying to index an integer (l[i+2]) when you should be indexing the slice (l[i:i+3]). You also need to copy the slice to avoid modifying the original data. 
Here's the corrected code:
func SortThird(l []int) []int {
    lCopy := make([]int, len(l))
    copy(lCopy, l)
    sort.Ints(lCopy)
    for i := 0; i < len(l); i += 3 {
        l[i], l[i+2] = lCopy[i+2], lCopy[i]
    }
    return l