
	min, max := math.MaxFloat64, -math.MaxFloat64

	for _, num := range numbers {
		if num < min {
			min = num
		}
		if num > max {
			max = num
		}
	}

	rescaled := make([]float64, len(numbers))
	for i, num := range numbers {
		rescaled[i] = (num - min) / (max - min)
	}

	return rescaled
}

// This function works by first finding the minimum and maximum values in the input list.
// Then, it creates a new list of the same length, replacing each value with the rescaled value.
// The rescaled value is computed as the original value subtracted by the minimum, divided by the range of the original values.
// This ensures that the smallest value in the original list becomes 0, and the largest value becomes 1.

// This function assumes that the input list contains at least two different values, 
// as it does not handle the case where all values in the input list are the same.
// It also assumes that the input list contains only numbers, as it does not check the type of the elements in the list.

// This function uses the math package to handle floating-point arithmetic, 
// which should be sufficient for most practical purposes.
// If the input list contains very large or very small numbers, 
// the precision of the floating-point arithmetic may be lost.
// In such cases, a different approach may be needed to handle the rescaling.

// This function returns a new list of rescaled values.
// It does not modify the original list.

// This function has a time complexity of O(n), 
// where n is the length of the input list, 
// because it performs a single pass over the input list to find the minimum and maximum values, 
// and another pass to rescale the values.

// This function has a space complexity of O(n), 
// where n is the length of the input list, 
// because it creates a new list of the same length as the input list.

// This function is safe for concurrent use by multiple goroutines,