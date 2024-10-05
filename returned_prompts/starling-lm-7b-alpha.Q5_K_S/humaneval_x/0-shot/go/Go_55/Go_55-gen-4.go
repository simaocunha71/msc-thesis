
if n == 0 {
return 0
}

if n == 1 {
return 1
}

var a = 0
var b = 1

for i := 2; i <= n; i++ {
a, b = b, a + b
}

return b
}

// Fibonacci sequence
// >>> fibs(10)
// [1 1 2 3 5 8 13 21 34 55]
func fibs(n int) []int {
res := make([]int, n)

for i := 0; i < n; i++ {
res[i] = Fib(i + 1)
}

return res
}

It's a Go program that calculates the Fibonacci sequence,
which is a sequence of numbers in which each number after the first two is the sum of the two preceding ones,
starting from 0 and 1.
In this program, the Fib function is used to calculate the n-th Fibonacci number,
and the fibs function is used to calculate the first n Fibonacci numbers.

To calculate the n-th Fibonacci number, the program first checks if n is 0 or 1, and returns 0 or 1 accordingly.
If n is not 0 or 1, the program uses a loop to calculate the n-th Fibonacci number iteratively, starting from 2.
The loop initializes two variables, a and b, with the values 0 and 1 respectively.
In each iteration, the values of a and b are swapped, and the value of a is updated to be the sum of the previous values of a and b.
After the loop, the program returns the value of b, which is the n-th Fibonacci number.

To calculate the first n Fibonacci numbers, the program initializes an array called res with a length of n.
Then, it uses a loop to calculate each Fibonacci number and assigns it to the corresponding index in the res array.
After the loop, the program returns the res array, which contains the first n Fibonacci numbers.

You can test the program by running it with different