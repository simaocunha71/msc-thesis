```javascript
const min = Math.min(...numbers);
const max = Math.max(...numbers);
const rescaledNumbers = numbers.map((num) => (num - min) / (max - min));
return rescaledNumbers;
```
Explanation:
1. We first find the minimum and maximum values in the list using the `Math.min` and `Math.max` functions with the spread operator (`...numbers`).
2. Then, we create a new list `rescaledNumbers` by applying the linear transformation to each number in the original list. The transformation is `(num - min) / (max - min)`, which maps the smallest number to 0 and the largest number to 1.
3. We use the `map` method to apply this transformation to each number in the original list.
4. The resulting list `rescaledNumbers` is returned.