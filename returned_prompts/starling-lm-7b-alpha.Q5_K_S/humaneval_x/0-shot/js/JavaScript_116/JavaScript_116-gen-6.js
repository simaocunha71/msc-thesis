Here is one way you could do it:

```javascript
function sortArray(arr) {
    return arr.sort((a, b) => {
        const countA = binCount(a);
        const countB = binCount(b);
        if (countA < countB) {
            return -1;
        } else if (countA > countB) {
            return 1;
        } else {
            return a - b;
        }
    });

    function binCount(num) {
        const bin = num.toString(2);
        return bin.split('').filter(x => x === '1').length;
    }
}
```
The idea here is to compare the count of '1's in the binary representation of the numbers. For the same number of '1's, the numbers themselves are compared to ensure the array is sorted by value.

The `binCount` function counts the number of '1's in the binary representation of a number.

```python
sortArray([1, 5, 2, 3, 4])  => [1, 2, 3, 4, 5]
sortArray([-2, -3, -4, -5, -6])  => [-6, -5, -4, -3, -2]
sortArray([1, 0, 2, 3, 4])  => [0, 1, 2, 3, 4]
```








































































































































































