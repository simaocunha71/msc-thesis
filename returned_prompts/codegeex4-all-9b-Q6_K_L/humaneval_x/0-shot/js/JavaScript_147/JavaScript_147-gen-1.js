To solve this problem, we need to understand the properties of the array `a`. 
The values of `a[i]` are calculated as `i * i - i + 1`. 
Since `i` is a positive integer, `i * i` is always a perfect square. 
The value of `i * i - i + 1` is always an odd number because it is a difference of two even numbers and an odd number. 
Therefore, the sum of any three numbers in the array `a` will always be a multiple of 3 if and only if each number is a multiple of 3.

Given this, we can count the number of multiples of 3 in the array `a` and return that count as the result.

Here is the complete code:

```javascript
const getMaxTriples = (n) => {
    let count = 0;
    for(let i = 1; i <= n; i++) {
        if(i % 3 === 0) {
            count++;
        }
    }
    return count;
}
```

This code iterates through the numbers from 1 to `n` and checks if each number is a multiple of 3. 
If it is, it increments the `count` variable. 
Finally, it returns the `count` variable, which represents the number of triples (a[i], a[j], a[k]) where i < j < k and a[i] + a[j] + a[k] is a multiple of 3.