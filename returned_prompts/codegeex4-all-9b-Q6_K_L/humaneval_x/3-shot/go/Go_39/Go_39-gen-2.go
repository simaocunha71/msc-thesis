
for i := 0; i < len(numbers); i++ {
    for j := i + 1; j < len(numbers); j++ {
        var distance float64 = math.Abs(numbers[i] - numbers[j])
        if distance < threshold {
            return true
        }
    }
}
return false

This is a double loop over all numbers in the slice. If there are many numbers, the time complexity will be high. This could be improved to O(n log n) with a sorted slice and a binary search.

for _, c := range paren_string {
    if c == '(' {
        current_depth += 1
        current_string = append(current_string, c)
    }else if c== ')'{
        current_depth -= 1
        current_string = append(current_string, c)

        if current_depth == 0{
            result = append(result, string(current_string))
            current_string =  make([]rune, 0)
        }
    }

}
return result

This is a loop over all characters in the string. If the string is long, the time complexity will be high. This could be improved to O(n) with a stack.

return math.Mod(number,1)

This is correct, but it could be more efficient to use integer arithmetic instead of floating point arithmetic.

for count < n {
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3

    if IsPrime(fib3) {
        count++
    }
}

This is correct, but it could be more efficient to check if a number is prime before adding it to the count.

func IsPrime(num int) bool {
    if num <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(num