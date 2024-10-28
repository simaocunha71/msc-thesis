
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

	diff := max - min
	res := make([]float64, len(numbers))

	for i, num := range numbers {
		res[i] = (num - min) / diff
	}

	return res
}

// 1. Find the min and max of the numbers
// 2. Calculate the difference (max - min)
// 3. Subtract the min from each number and divide the result by the difference to rescale the numbers to the range 0-1
// 4. Return the rescaled numbers

// This function takes a slice of float64 as input and returns a slice of float64. It first initializes min and max to be the first element of the input slice, then it iterates through the slice to find the minimum and maximum values. It then calculates the difference between the maximum and minimum, and creates a new slice of the same length as the input slice. It then iterates through the input slice again, subtracts the minimum from each number, and divides the result by the difference to rescale the numbers to the range 0-1. Finally, it returns the rescaled numbers.

```

### Python

```python
def rescale_to_unit(numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    diff = max_num - min_num
    return [(num - min_num) / diff for num in numbers]

# 1. Find the min and max of the numbers
# 2. Calculate the difference (max - min)
# 3. Subtract the min from each number and divide the result by the difference to rescale the numbers to the range 0-1
# 4. Return the rescaled numbers
```

## Pseudo-code

```
Function RescaleToUnit(numbers):
	min = numbers[0]
	max = numbers[0]

	For