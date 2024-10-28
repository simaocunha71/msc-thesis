
	sort.Float64s(numbers)

	smallestDiff := math.MaxFloat64
	var closestPair [2]float64

	for i := 0; i < len(numbers)-1; i++ {
		if diff := numbers[i+1] - numbers[i]; diff < smallestDiff {
			smallestDiff = diff
			closestPair[0] = numbers[i]
			closestPair[1] = numbers[i+1]
		}
	}

	return closestPair
}

// Test cases:
func main() {
	fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.2})) // (2.0, 2.2)
	fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.0})) // (2.0, 2.0)
}
```

This code first sorts the numbers array. Then it iterates through the sorted array and checks the difference between each pair of numbers. If the difference is smaller than the currently smallest difference, it updates the smallest difference and the pair of numbers. Finally, it returns the pair of numbers with the smallest difference.

This code also includes a test case to demonstrate its functionality.

## Discussion

In this solution, we first sort the numbers array. This is because we are looking for pairs of numbers that are closest to each other. Since the numbers are sorted, the pair of numbers that are closest to each other will be adjacent in the sorted array.

Next, we initialize the smallest difference to be the maximum float value and the closest pair to be an empty array. We then iterate through the sorted array and for each pair of numbers, we calculate their difference. If the difference is smaller than the smallest difference, we update the smallest difference and the closest pair.

Finally, we return the closest pair.

The time complexity of this solution is O(n log n) because of the sorting. The space complexity is O(1) because we are not using any additional space that scales with the input