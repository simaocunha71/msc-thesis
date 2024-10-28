func MakeAPile(n int) []int {
	var stones = []int{n}
	for i := 1; i < n; i++ {
		if n%2 == 0 {
			stones = append(stones, n+2*i)
		} else {
			stones = append(stones, n+2*i+1)
		}
	}
	return stones
}

func MakeAPile(n int) []int {
    stones := make([]int, n)
    for i := range stones {
        stones[i] = n + 2*i
    }
    if n%2 == 0 {
        stones[n-1]++
    }
    return stones
}

func MakeAPile(n int) []int {
    stones := make([]int, n)
    for i := range stones {
        stones[i] = n + 2*i + (i%2)
    }
    return stones
}

func MakeAPile(n int) []int {
    stones := make([]int, n)
    for i := range stones {
        stones[i] = n + 2*i + (i+1)%2
    }
    return stones
}