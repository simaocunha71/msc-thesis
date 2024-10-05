To solve this problem we need to first sort the given list of numbers. Then we can compare the adjacent numbers to find the closest pair. Here's a step-by-step explanation:

1. Sort the given list of numbers using the sort() method and a comparison function. The comparison function compares the absolute difference between two numbers. This way, the numbers will be sorted in ascending order.

2. Initialize two variables, minDiff and closestPair, to keep track of the minimum difference between two numbers and the closest pair of numbers, respectively. Set minDiff to infinity initially.

3. Iterate through the sorted list of numbers using a for loop, starting from the second element. For each number, compare it with the previous number using an if statement. Calculate the absolute difference between the two numbers and check if it's smaller than the current minimum difference. If it is, update minDiff and closestPair with the new values.

4. After the loop, return the closestPair, which will be the closest pair of numbers in ascending order.

Here's the code that implements the solution:

const findClosestElements = (numbers) => {
  numbers.sort((a, b) => Math.abs(a - b));
  
  let minDiff = Infinity;
  let closestPair = [];
  
  for (let i = 1; i < numbers.length; i++) {
    const diff = Math.abs(numbers[i] - numbers[i - 1]);
    if (diff < minDiff) {
      minDiff = diff;
      closestPair = [numbers[i - 1], numbers[i]];
    }
  }
  
  return closestPair;
};

To test the function, you can use the following code:

console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])); // (2.0, 2.2)
console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])); // (2.0, 2.0)

This will output the closest pairs of numbers