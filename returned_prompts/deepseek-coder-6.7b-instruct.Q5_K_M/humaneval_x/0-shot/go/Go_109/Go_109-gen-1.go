    for i := 0; i < len(arr); i++ {
        for j := 0; j < len(arr)-1; j++ {
            if arr[j] > arr[j+1] {
                arr[j], arr[j+1] = arr[j+1], arr[j]
            }
        }
    }

    for i := 0; i < len(arr)-1; i++ {
        if arr[i] > arr[i+1] {
            return false
        }
    }
    return true
}

```

The function MoveOneBall takes a slice of integers as input and returns a boolean.

The function works by first sorting the array in ascending order using a simple bubble sort algorithm. The sorting is done in a way that if any element in the array is greater than the next element, they are swapped. This is repeated until the entire array is sorted.

After the array is sorted, the function checks if the array is sorted in non-decreasing order. If it is, the function returns true. If not, the function returns false.

The function also handles the case where the input array is empty by returning true.

The time complexity of the function is O(n^2) due to the bubble sort algorithm, where n is the length of the array. The space complexity is O(1) as no additional space is used.

The function is used to solve the problem "Move One Ball".
*/

// CheckSorting check if the array is sorted in non-decreasing order
// after performing right shift operation any number of times.
func CheckSorting(arr []int) bool {

	n := len(arr)
	if n == 0 {
		return true
	}

	rotated := make([]int, n)
	copy(rotated, arr)

	sort.Ints(rotated)

	for i := 0; i < n; i++ {

		// Check if arr is a right rotation of sorted
		isRightRotation := true
		for j := 0; j < n; j++ {
			if arr[j] != rotated[(i+j)%n] {
				