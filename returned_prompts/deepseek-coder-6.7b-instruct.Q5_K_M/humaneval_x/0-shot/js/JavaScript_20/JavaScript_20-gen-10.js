  let closestPair = [Infinity, null, null];
  for(let i = 0; i < numbers.length; i++){
    for(let j = i + 1; j < numbers.length; j++){
      const diff = Math.abs(numbers[i] - numbers[j]);
      if(diff < closestPair[0]){
        closestPair = [diff, numbers[i], numbers[j]];
      }
    }
  }
  return [Math.min(closestPair[1], closestPair[2]), Math.max(closestPair[1], closestPair[2])];
}

console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])); // (2.0, 2.2)
console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])); // (2.0, 2.0)


In the above solution, we initialize the variable `closestPair` to [Infinity, null, null], which will hold the smallest difference found so far, and the two numbers that produced this difference. We then iterate over each possible pair of numbers, calculate their difference, and if this difference is smaller than the current smallest difference, we update `closestPair`. Finally, we return the two numbers that produced the smallest difference in ascending order.
*/

/*
The time complexity of the above code is O(n^2) because we are iterating through the numbers array twice. The space complexity is O(1) because we are not using any extra space proportional to the size of the input array.
*/

/*
The code above works fine but it's not optimal. It's because we are trying to solve a problem in the most straightforward way. It's possible to solve this problem in O(n log n) time complexity and O(1) space complexity. This solution will use sorting and then iterate through the array to find the smallest difference. But it's a bit more complex.
*/

/*
Here is the optimized code:

const findClos