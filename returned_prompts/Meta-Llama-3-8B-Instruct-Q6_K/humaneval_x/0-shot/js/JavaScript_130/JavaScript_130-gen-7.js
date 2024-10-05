Here is the JavaScript solution for the problem:

```javascript
function tri(n) {
    if (n === 0) {
        return [];
    }
    if (n === 1) {
        return [3];
    }
    if (n === 2) {
        return [3, 2];
    }
    const tribonacci = [3, 2];
    for (let i = 2; i < n; i++) {
        if (i % 2 === 0) {
            tribonacci.push(1 + i / 2);
        } else {
            const a = tribonacci[i - 1];
            const b = tribonacci[i - 2];
            const c = tribonacci[i - 3];
            tribonacci.push(a + b + c);
        }
    }
    return tribonacci;
}
```
This function takes an integer `n` as an argument and returns a list of the first `n + 1` numbers of the Tribonacci sequence. It uses a for loop to generate the sequence. The base cases for the recursion are handled separately. If `n` is 0, the function returns an empty list. If `n` is 1 or 2, the function returns the base cases for the Tribonacci sequence. For `n` greater than 2, the function uses a for loop to generate the sequence. If `n` is even, the function calculates the next number in the sequence as `1 + n / 2`. If `n` is odd, the function calculates the next number in the sequence as the sum of the last three numbers in the sequence. The function returns the list of the first `n + 1` numbers of the Tribonacci sequence.