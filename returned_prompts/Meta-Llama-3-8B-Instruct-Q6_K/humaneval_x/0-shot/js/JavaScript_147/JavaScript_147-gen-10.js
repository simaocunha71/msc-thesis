```
let count = 0;
let a = [];
for (let i = 1; i <= n; i++) {
    a.push(i * i - i + 1);
}
for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
        for (let k = j + 1; k < n; k++) {
            if ((a[i] + a[j] + a[k]) % 3 === 0) {
                count++;
            }
        }
    }
}
return count;
```
This solution first creates an array `a` of length `n` with the given formula. Then, it uses three nested loops to iterate over all possible triples `(a[i], a[j], a[k])` and checks if the sum of the triple is a multiple of 3. If it is, it increments the `count` variable. Finally, it returns the `count` variable, which represents the number of triples that satisfy the condition.