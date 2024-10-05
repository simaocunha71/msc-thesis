
// initialize a new empty list to store the positive numbers
positive := []int{}

// iterate over the list
for _, value := range l {
    // if the number is positive
    if value > 0 {
        // add it to the list of positive numbers
        positive = append(positive, value)
    }
}

// return the list of positive numbers
return positive
}
```

## Task 2: Fibonacci Sequence

Write a function that returns a specified number of elements of the Fibonacci sequence. The Fibonacci sequence is a sequence of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

```python
