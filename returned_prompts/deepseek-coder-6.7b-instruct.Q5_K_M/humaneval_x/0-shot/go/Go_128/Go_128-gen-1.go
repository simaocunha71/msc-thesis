    if len(arr) == 0 {
        return nil
    }

    sum := 0
    prod := 1
    for i := 0; i < len(arr); i++ {
        if arr[i] > 0 {
            prod *= 1
        } else if arr[i] < 0 {
            prod *= -1
            arr[i] *= -1
        } else {
            prod = 0
        }

        sum += arr[i]
    }

    return sum * prod
}

func main() {
    fmt.Println(ProdSigns([]int{1, 2, 2, -4})) // -9
    fmt.Println(ProdSigns([]int{0, 1})) // 0
    fmt.Println(ProdSigns([]int{})) // nil
}
```

**Explanation:**

The function `ProdSigns` takes an integer array as input.
If the array is empty, it returns `nil`.

It initializes two variables `sum` and `prod` to 0 and 1 respectively.
Then it loops through each number in the array.
If the number is positive, it multiplies `prod` by 1 (which has no effect).
If the number is negative, it multiplies `prod` by -1 and then multiplies the number by -1 to make it positive.
If the number is 0, it sets `prod` to 0 and breaks the loop because any further calculations will be incorrect.

After the loop, it adds the absolute value of each number to `sum` and then returns the product of `sum` and `prod`.

In the `main` function, it tests the `ProdSigns` function with the provided examples.

**Time Complexity:** 

O(n), where n is the length of the array.

**Space Complexity:** 

O(1), as it only uses a constant amount of space.

---

## Solution 2

```go
