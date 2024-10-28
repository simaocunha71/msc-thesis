  return [...new Set(l1.filter(i => l2.includes(i)).sort((a, b) => a - b))];

};

console.log(common([1, 4, 3, 34, 653, 2, 5],[5, 7, 1, 5, 9, 653, 121]));
console.log(common([5, 3, 2, 8],[3, 2]));




A: Here is the solution:


const common = (l1, l2) => {
  return [...new Set(l1.filter(i => l2.includes(i)).sort((a, b) => a - b))];
};

console.log(common([1, 4, 3, 34, 653, 2, 5],[5, 7, 1, 5, 9, 653, 121]));
console.log(common([5, 3, 2, 8],[3, 2]));


In the above solution:

*

*We first filter the elements of the first list (l1) which exist in the second list (l2). This is done using the filter() method.

*We then create a Set from the resulting array to remove any duplicate values. A Set is a special type of object that only allows unique values.

*Finally, we sort the array in ascending order using the sort() method.

*The spread operator (...) is used to convert the Set back to an array.

*The sort() method is used with a comparison function ((a, b) => a - b) to sort the numbers in ascending order.


A: This solution uses JavaScript's built-in array methods and the Set object:


const common = (arr1, arr2) => {
  let set1 = new Set(arr1);
  let set2 = new Set(arr2);
  return [...new Set([...set1].filter(i => set2.has(i)).sort((a, b) => a - b))];
};

console.