    sort.Sort(sort.Reverse(sort.IntSlice(arr)))

B:
    return arr[:k]
}


A: The array is first sorted in reverse order. This means that the highest numbers are at the start of the array.

B: Then, a slice of the array from index 0 to k (non-inclusive) is returned. This slice contains the maximum k numbers from the original array.

This solution has a time complexity of O(n log n) due to the sorting operation, where n is the length of the input array. The space complexity is O(k) because we need to store the k maximum numbers.
*/

func Maximum(arr []int, k int) []int {
	sort.Sort(sort.Reverse(sort.IntSlice(arr)))
	return arr[:k]
}

// 2nd approach
/*
func Maximum(arr []int, k int) []int {
	heap := &IntHeap{}
	heap.Init()

	for _, value := range arr {
		heap.Push(value)
	}

	result := make([]int, k)
	for i := 0; i < k; i++ {
		result[i] = heap.Pop().(int)
	}

	return result
}

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func (h *IntHeap) Init() {
	heap.Init(