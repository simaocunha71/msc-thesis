
const arrayCopy = [...array];
const firstIndex = 0;
const lastIndex = arrayCopy.length - 1;

if ((arrayCopy[firstIndex] + arrayCopy[lastIndex]) % 2 === 0) {
  arrayCopy.sort((a, b) => b - a);
} else {
  arrayCopy.sort((a, b) => a - b);
}

return arrayCopy;
};

sortArray([2, 4, 3, 0, 1, 5, 6]);


Answer:
To solve this problem, we can follow these steps:

Create a copy of the given array, since we don't want to change the original array.
Calculate the sum of the first and last elements of the array. If it's even, we will sort the array in descending order. If it's odd, we will sort the array in ascending order.
Sort the copied array in the desired order using the `sort` method and a comparison function.
Return the sorted array.

In the provided solution, we first create a copy of the input array using the spread operator `[...array]`. Then we define the indices of the first and last elements of the copied array.

Next, we check if the sum of the first and last elements is even by using the modulo operator `%` to check if the sum is divisible by 2. If it is, we sort the copied array in descending order using the `sort` method and a comparison function `(a, b) => b - a`. If the sum is odd, we sort the copied array in ascending order using the `sort` method and a comparison function `(a, b) => a - b`.

Finally, we return the sorted array.

When we call `sortArray([2, 4, 3, 0, 1, 5, 6])`, the function will create a copy of the array `[2, 4, 3, 0, 1, 5, 6]`. Since the sum of the first and last elements (2 + 6) is even, the function will sort the copied array in descending order, resulting in `[6, 5, 4, 3, 2, 1,