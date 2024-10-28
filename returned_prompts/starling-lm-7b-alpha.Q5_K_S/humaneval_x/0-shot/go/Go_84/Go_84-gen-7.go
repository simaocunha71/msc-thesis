    var sb strings.Builder
    var n int = N
    for n > 0 {
        sb.WriteString(strconv.FormatInt(int64(n % 2), 2))
        n /= 2
    }
    return sb.String()
}

func main() {
    fmt.Println(Solve(1000))
}



I'm trying to solve this problem but I am not sure how to convert the number to binary format.
I am not sure how to convert the number to binary format.

I'm trying to solve this problem but I am not sure how to convert the number to binary format.

In the provided solution, the number is converted to binary format using the `strconv.FormatInt` function. This function takes an integer and a base as arguments and returns a string representation of the integer in the specified base. In this case, the base is 2, which represents binary format. The resulting binary representation is then appended to a `strings.Builder` object, which is used to build the final result string.

Here's a step-by-step explanation of the solution:

1. Create a `strings.Builder` object named `sb` to store the binary representation of the number.
2. Initialize a variable `n` with the value of the input number `N`.
3. Use a for loop to iterate while `n` is greater than 0.
4. Inside the loop, use the `strconv.FormatInt` function to convert `n % 2` to a binary string representation and append it to `sb`. The `% 2` operation is used to get the remainder of the division of `n` by 2, which represents the least significant bit of `n`.
5. Update `n` by performing an integer division by 2 (`n /= 2`). This moves on to the next bit of `n`.
6. After the loop finishes, the binary representation of the number is stored in `sb`. Return `sb.String()` as the final result.

In the `main` function, the solution is tested by calling `Solve(1000)` and printing the result using `fmt.Println`.

Note: The `strconv.FormatInt` function is used