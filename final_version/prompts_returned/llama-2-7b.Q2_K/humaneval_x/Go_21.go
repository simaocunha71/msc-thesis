
// Given list of numbers (of at least two elements), apply a linear transform to that list,
// such that the smallest number will become 0 and the largest will become 1
// >>> RescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0])
// [0.0, 0.25, 0.5, 0.75, 1.0]
func RescaleToUnit(numbers []float64) []float64 {
	if len(numbers) < 2 {
		return numbers
	}
	sum := rescaleSum(numbers[0:])
	if numbers[0] == sum || numbers[len(numbers)-1] == sum {
		for i, n := range numbers {
			n = n + (sum-n) / 2
		}
	} else { // we have to do some math to get the right order.
		temp := copy(numbers[0:])
		i := 1
		for ; i < len(numbers); i++ {
			if temp[i] > numbers[len(numbers)-1], temp = append(temp, -1), n := -n-1 {
				continue
			} else if temp[i] == 0 || temp[i] < 0, n *= -2.0, break
		}
		if len(numbers) > 3, n += 1/6 + (n+0.5)*0.2 / (float64(len(temp))-float64(i)); // TODO, this is just an example
		copy(numbers[0:], temp[0:])
	}
	return numbers;
}
