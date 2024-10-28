
// First, we need to find the smallest even number in the array. We can do this by using a for loop to iterate through each node in the array and checking if the node's value is even (i.e., it is divisible by 2). If it is, we keep track of the smallest even number and its index using a pair of variables, minValue and minIndex. Here's an example of how to do this:

let minValue = Infinity;
let minIndex = -1;
for (let i = 0; i < arr.length; i++) {
  const node = arr[i];
  if (node % 2 === 0 && node < minValue) {
    minValue = node;
    minIndex = i;
  }
}

// Next, we need to return the smallest even number and its index in a list format. We can do this by creating a new array with the minValue and minIndex as its elements, and then returning this array. Here's an example of how to do this:

return [minValue, minIndex];

// Finally, we need to handle the case where there are no even values in the array. In this case, the minValue will still be Infinity and the minIndex will still be -1, so we can simply return an empty array to indicate that there are no even values to pluck. Here's an example of how to do this:

if (minValue === Infinity) {
  return [];
} else {
  return [minValue, minIndex];
}

 */

};



// Test cases
console.log(pluck([])); // []
console.log(pluck([4, 2, 3])); // [2, 1]
console.log(pluck([1, 2, 3])); // [2, 1]
console.log(pluck([5, 0, 3, 0, 4, 2])); // [0, 1]




























































