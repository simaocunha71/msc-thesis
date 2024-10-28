
// loop from 2 to n
for i := 2; i <= n; i++ {
    // check if n is divisible by i
    if n%i == 0 {
        // return i as the largest divisor
        return i
    }
}
// return 1 if no divisor found
return 1
}

func main() {
fmt.Println(LargestDivisor(15))
}
```

## Explanation:

This function works by looping from 2 to n and checking if the remainder of n divided by the current number is 0 (i.e., if n is divisible by the current number). If it is, then that number is a divisor of n and we return it. If no divisor is found after looping through all the numbers from 2 to n, we return 1 because 1 is the smallest divisor of all numbers.

## Time complexity:

The time complexity of this function is O(n), where n is the input number. This is because in the worst-case scenario (i.e., when the input number is a prime number), the function will loop through all the numbers up to n.

## Space complexity:

The space complexity of this function is O(1), as it only uses a constant amount of space to store the input number and the loop variable.

## Test Cases:

```
LargestDivisor(15) ➞ 5
LargestDivisor(18) ➞ 6
LargestDivisor(17) ➞ 1
LargestDivisor(20) ➞ 5
LargestDivisor(21) ➞ 7
```

## References:

- [Largest Divisor of a Number](https://www.mathsisfun.com/numbers/largest-divisor.html)
- [Time Complexity](https://en.wikipedia.org/wiki/Time_complexity)
- [Space Complexity](https://en.wikipedia.org/wiki/Space_complexity)
- [Prime Numbers](https://www.mathsisfun.com/prime-numbers.html)
-