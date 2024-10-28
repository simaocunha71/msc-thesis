[num.toString().split('').reduce((a, b) => {
    return b % 2 ? a[1]++ : a[0]++;
}, {0: 0, 1: 0}), num.toString().split('').reduce((a, b) => {
    return b % 2 ? a[1]++ : a[0]++;
}, {0: 0, 1: 0})]

Explanation:
The reduce() method reduces the array to a single value by applying a function to each element in the array.
In this case, the initial values for the reductions are objects with two properties, 0 and 1, representing the even and odd counts respectively.
The reduce() function is called twice, first to count the even numbers, and then to count the odd numbers.
The split() method splits the string representation of the number into an array of digits.

Here is a breakdown of the code:

    num.toString().split('') - Converts the number to a string and splits it into an array of characters.
    reduce((a, b) => { ... }, {0: 0, 1: 0}) - Reduces the array to a single value by applying the provided function and initializing the result with the given object.
    b % 2 ? a[1]++ : a[0]++ - Conditionally increments the appropriate count (even or odd) based on whether the current digit is odd or even.

The result is an array with two elements: the count of even digits and the count of odd digits.

For example, for the input -12, the code will return [1, 1] because there is one even digit (2) and one odd digit (1).
For the input 123, the code will return [1, 2] because there is one even digit (2) and two odd digits (1 and 3).

*/










































































