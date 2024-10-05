    var res []int
    for _, v := range x {
        if !containEven(v) {
            res = append(res, v)
        }
    }
    sort.Sort(sort.IntSlice(res))
    return res
}

func containEven(n int) bool {
    for n > 0 {
        if n%2 == 0 {
            return true
        }
        n /= 10
    }
    return false
}





I'm having trouble understanding this part of the code:

res = append(res, v)

Why do we need to use append?

In addition, why do we need to sort the result?

It seems to me that the code is already sorted, as we only append to res when v is not even.

Here is a brief explanation of the code:

The function UniqueDigits takes in a slice of integers and returns a sorted slice of integers that do not contain any even digits.

The function containEven checks if a number has an even digit. It does this by repeatedly dividing the number by 10 until it becomes 0. If at any point the number is divisible by 2, it means the number has an even digit and the function returns true. If the function reaches 0 without finding an even digit, it returns false.

The function UniqueDigits iterates over each number in the input slice. For each number, it checks if it does not contain any even digit using the containEven function. If the number passes this check, it is appended to the result slice res.

Finally, the result slice is sorted using the sort.Sort function from the sort package. This is done to ensure that the numbers in the result slice are in ascending order, as required by the problem statement.

As for why append is used instead of simply assigning the value to res directly, it's because append is more efficient when appending to a slice. It allocates memory only when necessary, which can be more efficient than assigning to a slice if the slice needs to be resized repeatedly.

I hope this helps clarify the code! Let me know if you have any more questions.





As for why the result needs to be sorted, it