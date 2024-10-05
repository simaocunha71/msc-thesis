
	sum := x.(int) + y.(int) + z.(int)
	
	if x.(int) == sum || y.(int) == sum || z.(int) == sum {
		return true
	}
	
	return false
}




// Create a function that takes an array of numbers and returns the total sum of all numbers in the array.
// However, if any of the numbers is a string that can be converted into an integer, convert it into an integer and sum it.
// If the array contains any other data type, do not include it in the sum.
// 
// Examples
// SumOrConvert([1, 2, '3']) ➞ 6
// 
// SumOrConvert([1, '200', 3, '400']) ➞ 601
// 
// SumOrConvert([1, 2, 'abc']) ➞ 3
// 
// SumOrConvert([1, 2, '3', '4.5']) ➞ 7
func SumOrConvert(arr []interface{}) int {

B:

	sum := 0
	
	for _, v := range arr {
		switch v := v.(type) {
		case int:
			sum += v
		case string:
			if i, err := strconv.Atoi(v); err == nil {
				sum += i
			}
		default:
			continue
		}
	}
	
	return sum
}




// Create a function that takes an array of integers and returns the difference between the largest and smallest numbers.
// 
// Examples
// DifferenceMaxMin([10, 4, 1, 4, -10, -50]) ➞ 50
// 
// DifferenceMaxMin([44, 32, 56, 85, 2, 7, 9]) ➞ 89
// 
// DifferenceMaxMin([23, 12, 6, 18, 29]) ➞ 21
func DifferenceMaxMin(arr []int) int {

