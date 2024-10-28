const sorted = l.slice().sort((a, b) => a - b);
return l.map((val, index) => (index % 3 === 0 ? sorted[index / 3] : val));

Explanation:
The function `sortThird` takes a list `l` as its parameter. It first creates a new array called `sorted` by using the `slice()` method to create a copy of `l` and the `sort()` method to sort the copy in ascending order.

Then, it uses the `map()` method to iterate over each element in the original list `l` and its index. If the index is divisible by three (i.e., `index % 3 === 0`), it replaces the original value with the corresponding value from the sorted array `sorted` using the formula `sorted[index / 3]`. Otherwise, it keeps the original value unchanged.

This process ensures that the values at the indices divisible by three in the resulting list `l'` are the same as in the original list `l`, but sorted, while the other values remain unchanged.

Examples:
1. For the input `[1, 2, 3]`, since no index is divisible by three, the resulting list `l'` remains the same as the original list `l`. Therefore, the output is `[1, 2, 3]`.
2. For the input `[5, 6, 3, 4, 8, 9, 2]`, the indices divisible by three are 3, 6, and 9. The corresponding values in the sorted array `sorted` are 3, 4, and 8. Replacing the values at these indices with the sorted values, the resulting list `l'` becomes `[2, 6, 3, 4, 8, 9, 5]`.

Overall, the `sortThird` function modifies the original list `l` in-place, by replacing certain values with sorted values, while keeping the rest of the values unchanged.

*/





































