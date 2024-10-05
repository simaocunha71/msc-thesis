let max = l[0];
for(let i = 1; i < l.length; i++){
  if(l[i] > max){
    max = l[i]
  }
}
return max;
}


A: You can also use the built-in JavaScript functions Math.max() and apply it to the array.


const maxElement = l => Math.max(...l);

console.log(maxElement([1, 2, 3])); // 3
console.log(maxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])); // 123


The function Math.max() returns the largest of zero or more numbers. The spread operator (...) allows us to pass in the elements of the array as individual arguments to the Math.max() function.

A: Here is a more concise version using the reduce method:


const maxElement = l => l.reduce((max, cur) => cur > max ? cur : max);

console.log(maxElement([1, 2, 3])); // 3
console.log(maxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])); // 123


This function works by iterating over each element in the list and comparing it to the current maximum (initialized to the first element in the list). If the current element is larger than the current maximum, it becomes the new maximum. Otherwise, the current maximum remains unchanged. At the end of the iteration, the maximum element has been found.

A: Here is a one-liner solution using the spread operator (...) and Math.max function:


const maxElement = (l) => Math.max(...l);

console.log(maxElement([1, 2, 3])); // 3
console.log(maxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])); // 123

