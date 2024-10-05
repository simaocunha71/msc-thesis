Here is a JavaScript function that calculates the first n+1 numbers of the Tribonacci sequence:

```javascript
function tri(n) {
    if (n <= 0) {
        return [];
    }
    if (n === 1) {
        return [3];
    }
    if (n === 2) {
        return [3, 2];
    }
    let result = [3, 2];
    for (let i = 3; i <= n; i++) {
        if (i % 2 === 0) {
            result.push(1 + i / 2);
        } else {
            result.push(result[i - 1] + result[i - 2] + result[i - 3]);
        }
    }
    return result;
}
```

This function first checks the base cases (n <= 0, n === 1, n === 2) and returns the corresponding lists. Then it initializes the result list with the first two elements of the Tribonacci sequence, and uses a for loop to calculate the rest of the sequence. In each iteration, it checks if the current number is even or odd, and uses the corresponding formula to calculate the next number in the sequence. Finally, it returns the result list.