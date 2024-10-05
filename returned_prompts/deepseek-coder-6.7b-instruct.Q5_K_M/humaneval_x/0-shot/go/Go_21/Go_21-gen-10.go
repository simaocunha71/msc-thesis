
	min, max := minmax(numbers)
	rescaled := make([]float64, len(numbers))

	for i, num := range numbers {
		rescaled[i] = (num - min) / (max - min)
	}

	return rescaled
}

func minmax(numbers []float64) (float64, float64) {
	min := numbers[0]
	max := numbers[0]

	for _, num := range numbers {
		if num < min {
			min = num
		}
		if num > max {
			max = num
		}
	}

	return min, max
}

```

## Solution

```go

