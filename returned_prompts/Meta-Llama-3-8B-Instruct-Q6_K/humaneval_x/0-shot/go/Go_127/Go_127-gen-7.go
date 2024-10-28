```go
func Intersection(interval1 [2]int, interval2 [2]int) string {
    start := math.Max(float64(interval1[0]), float64(interval2[0]))
    end := math.Min(float64(interval1[1]), float64(interval2[1]))
    if start > end {
        return "NO"
    }
    length := int(end - start + 1)
    isPrime := true
    for i := 2; i * i <= length; i++ {
        if length%i == 0 {
            isPrime = false
            break
        }
    }
    if isPrime {
        return "YES"
    }
    return "NO"
}
```


This function calculates the intersection of the two given intervals and checks if its length is a prime number. It first calculates the start and end of the intersection by comparing the start and end points of the two intervals. If the intersection is empty (i.e., start > end), it returns "NO". Then it calculates the length of the intersection by subtracting the start from the end and adding 1. It checks if the length is a prime number by iterating from 2 to the square root of the length and checking if the length is divisible by any of these numbers. If the length is a prime number, it returns "YES", otherwise "NO".  The function uses the math.Max and math.Min functions to compare the start and end points of the intervals. The function uses the isPrime variable to keep track of whether the length is a prime number. The function uses the break statement to exit the loop if it finds a divisor of the length.  The function returns "YES" if the length is a prime number, and "NO" otherwise.  The function uses the float64 type to perform the calculations, and the int type to convert the result to an integer.  The function uses the math.Min function to find the minimum of the start and end points of the intervals, and the math.Max function to find the maximum of the start and end points of the intervals.  The function uses the % operator to check if the length is divisible by any of the numbers from 2 to the square root of the length.  The function uses the break statement to exit the loop if it finds a divisor of the length.  The function uses the return statement to return the result.  The function uses the string type to return the result as a string.  The function uses the "YES" and "NO"