Here is the solution for the problem:

```javascript
const orderByPoints = (nums) => {
    return nums.sort((a, b) => {
        let sumA = a.toString().split('').reduce((acc, current) => acc + parseInt(current), 0);
        let sumB = b.toString().split('').reduce((acc, current) => acc + parseInt(current), 0);
        if (sumA === sumB) {
            return nums.indexOf(a) - nums.indexOf(b);
        } else {
            return sumA - sumB;
        }
    });
};
```


Here is the explanation of the solution:

The function `orderByPoints` takes an array of integers as an argument. It returns a new array with the same elements as the input array, but sorted in ascending order based on the sum of their digits. If there are several items with the same sum of their digits, they are ordered based on their index in the original list.

The function uses the `sort` method of the array, which sorts the array in place and returns the sorted array. The `sort` method takes a compare function as an argument, which is used to compare two elements of the array. The compare function returns a negative value if the first element is smaller than the second element, a positive value if the first element is larger than the second element, and 0 if the two elements are equal.

In this implementation, the compare function calculates the sum of the digits of each element by converting the element to a string, splitting the string into an array of characters, and reducing the array to a sum using the `reduce` method. If the sums of the digits of the two elements are equal, the compare function returns the difference between the indices of the two elements in the original array. Otherwise, it returns the difference between the sums of the digits.

The `indexOf` method is used to get the index of an element in the original array. This is used to order elements with the same sum of their digits based on their original order.

The function returns the sorted array.