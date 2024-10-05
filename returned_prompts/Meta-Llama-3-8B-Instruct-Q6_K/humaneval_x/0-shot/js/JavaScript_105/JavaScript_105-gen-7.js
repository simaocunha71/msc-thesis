Here is a JavaScript solution for the problem:

```javascript
function byLength(arr) {
    const digitNames = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'];
    return arr.filter(num => num >= 1 && num <= 9).sort((a, b) => a - b).reverse().map(num => digitNames[num - 1]);
}
```
This function filters the array to include only numbers between 1 and 9, sorts them, reverses the array, and then maps each number to its corresponding digit name. The result is an array of strings representing the digit names in the desired order. If the input array is empty, the function returns an empty array. If the array contains any numbers outside the range 1-9, they are ignored. For example, the function would return `["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]` for the input array `[2, 1, 1, 4, 5, 8, 2, 3]`.