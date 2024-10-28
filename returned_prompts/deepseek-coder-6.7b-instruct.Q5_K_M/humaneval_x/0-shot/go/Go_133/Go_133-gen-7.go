    var sum float64
    for _, v := range lst {
        v = math.Ceil(v)
        sum += math.Pow(v, 2)
    }
    return int(sum)
}

// Time complexity: O(n)
// Space complexity: O(1)

*/

func SumSquares(lst []float64) int {
	var sum float64
	for _, v := range lst {
		v = math.Ceil(v)
		sum += math.Pow(v, 2)
	}
	return int(sum)
}

// Time complexity: O(n)
// Space complexity: O(1)

/*

