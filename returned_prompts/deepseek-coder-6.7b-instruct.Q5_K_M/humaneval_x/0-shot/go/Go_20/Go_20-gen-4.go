
	sort.Float64s(numbers)
	
	minDiff := math.MaxFloat64
	var closestElements [2]float64
	
	for i := 0; i < len(numbers) - 1; i++ {
		if diff := numbers[i+1] - numbers[i]; diff < minDiff {
			minDiff = diff
			closestElements[0] = numbers[i]
			closestElements[1] = numbers[i+1]
		}
	}
	
	return closestElements
}

// Test cases
func main()  {
	
	test1 := FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.2})
	fmt.Println(test1) // Should print [2.0, 2.2]
	
	test2 := FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.0})
	fmt.Println(test2) // Should print [2.0, 2.0]
}

```

## Concepts:

- Sorting
- Arrays
- Loops
- Conditional Statements

## Lesson:

In this lesson, we learned how to find the two numbers in a list that are closest to each other. We used the `sort` package in Go to sort the list of numbers and then looped through the list to find the two numbers with the smallest difference. If the difference is less than the current smallest difference, we updated the smallest difference and the pair of numbers. At the end, we returned the pair of numbers with the smallest difference.

## Key Takeaways:

- Sorting a list of numbers can be done using the `sort.Float64s` function in Go.
- Looping through a list of numbers can be done using a for loop.
- Comparing the difference between two numbers can be done using subtraction.
- If a condition is true, the code inside the if block will be executed.
- Arrays in Go are zero-indexed, meaning