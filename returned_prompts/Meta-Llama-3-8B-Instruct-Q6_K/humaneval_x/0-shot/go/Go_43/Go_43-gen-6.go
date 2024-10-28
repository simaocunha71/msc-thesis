```
    for i := 0; i < len(l); i++ {
        for j := i + 1; j < len(l); j++ {
            if l[i]+l[j] == 0 {
                return true
            }
        }
    }
    return false
}
```


The function PairsSumToZero takes a list of integers as an input. It iterates over the list with two nested loops to check if there are two distinct elements that sum to zero. If such a pair is found, it returns true. If no such pair is found after checking all possible pairs, it returns false.

The time complexity of this function is O(n^2) where n is the length of the input list, because it has a quadratic number of comparisons. The space complexity is O(1), because it only uses a constant amount of space to store the indices and the elements.

This function is not efficient for large lists, because it has a quadratic time complexity. It's better to use a more efficient algorithm, such as sorting the list and then iterating over it to find the pair that sums to zero. However, this function is simple and works well for small lists.