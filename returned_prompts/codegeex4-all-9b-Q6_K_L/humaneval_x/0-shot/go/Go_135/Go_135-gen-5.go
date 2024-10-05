func CanArrange(arr []int) int {
	for i := range arr {
		if i == 0 {
			continue
		}
		if arr[i] < arr[i-1] {
			return i
		}
	}
	return -1
}