```
function pairsSumToZero(l) {
    for (let i = 0; i < l.length; i++) {
        for (let j = i + 1; j < l.length; j++) {
            if (l[i] + l[j] === 0) {
                return true;
            }
        }
    }
    return false;
}
```


Here's how the function works:

1. It iterates over each element in the list using a nested loop.
2. For each pair of elements, it checks if the sum of the pair is equal to 0.
3. If it finds a pair that sums to 0, it immediately returns `true`.
4. If it doesn't find any pairs that sum to 0, it returns `false` after iterating over the entire list.

This function has a time complexity of O(n^2), where n is the length of the input list. This is because it uses a nested loop to iterate over the list. The space complexity is O(1), which means the function uses a constant amount of space.