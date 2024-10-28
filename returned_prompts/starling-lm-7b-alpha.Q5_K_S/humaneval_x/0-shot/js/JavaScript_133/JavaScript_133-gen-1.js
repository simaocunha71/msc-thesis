lst.map(num => Math.ceil(num)).reduce((acc, curr) => acc + Math.pow(curr, 2), 0)

/*
Explanation:
The function first maps through each number in the array and rounds them up to the nearest whole number using the Math.ceil() function.
Then, it uses the reduce() function to add up all the squares of each number in the array, starting from 0.

This will return the sum of squared numbers in the given list, with each element rounded up to the nearest whole number.

Note: The Math.ceil() function rounds a number up to the nearest whole number.
*/

*/

Answer:
The function first maps through each number in the array and rounds them up to the nearest whole number using the Math.ceil() function. Then, it uses the reduce() function to add up all the squares of each number in the array, starting from 0. This will return the sum of squared numbers in the given list, with each element rounded up to the nearest whole number.

Here's a step-by-step breakdown of how the function works:

1. The function uses the map() method to iterate over each element in the input array, lst. For each element, it uses the Math.ceil() function to round the number up to the nearest whole number. This ensures that all the numbers in the array are integers.

2. After mapping the array, the function uses the reduce() method to add up all the squares of each number in the array, starting from 0. The reduce() method takes a callback function as an argument, which is executed for each element in the array. The callback function takes two parameters, acc (short for accumulator) and curr (short for current). The acc parameter represents the accumulated value of the sum, while the curr parameter represents the current element in the array.

3. Inside the reduce() callback function, the acc parameter is updated by adding the square of the current element (Math.pow(curr, 2)). This means that for each element in the array, the square of that element is added to the accumulated sum.

4. Finally, the reduce() method returns the total sum of the squares of all the numbers in the input array.

In summary, the function sumSquares(lst