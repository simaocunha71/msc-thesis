```
result := 0
for i, v := range lst {
    if i % 2 == 1 && v % 2 == 0 {
        result += v
    }
}
return result
```


This code defines a function `Add` that takes a list of integers `lst` as input and returns the sum of the even elements that are at odd indices in the list.

The function uses a for loop with a range variable `i` that iterates over the indices of the list, and a variable `v` that takes the value of the element at the current index.

The condition `i % 2 == 1` checks if the current index is odd, and the condition `v % 2 == 0` checks if the element at the current index is even. If both conditions are true, the element is added to the result.

Finally, the function returns the result, which is the sum of the even elements at odd indices.