  const sortedArray = [...array];
  const firstElem = sortedArray[0];
  const lastElem = sortedArray[sortedArray.length - 1];

  if ((firstElem + lastElem) % 2 === 0) {
    sortedArray.sort((a, b) => b - a);
  } else {
    sortedArray.sort((a, b) => a - b);
  }

  return sortedArray;
};
*/

const sortArray = (array) => {
  const sortedArray = [...array];
  const firstElem = sortedArray[0];
  const lastElem = sortedArray[sortedArray.length - 1];

  if ((firstElem + lastElem) % 2 === 0) {
    sortedArray.sort((a, b) => b - a);
  } else {
    sortedArray.sort((a, b) => a - b);
  }

  return sortedArray;
};

console.log(sortArray([]));
console.log(sortArray([5]));
console.log(sortArray([2, 4, 3, 0, 1, 5]));
console.log(sortArray([2, 4, 3, 0, 1, 5, 6]));




// Solution: 
/*
This solution creates a copy of the array, then sorts it based on the sum of the first and last elements in the array. 
If the sum is even, it sorts in descending order, else it sorts in ascending order.
*/










































































































































