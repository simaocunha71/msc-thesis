  for(let i = 0; i < l.length; i++){
    if(l[i] >= t){
      return false
    }
  }
  return true
}

console.log(belowThreshold([1, 2, 4, 10], 100)) // true
console.log(belowThreshold([1, 20, 4, 10], 5)) // false

*/

const belowThreshold = (l, t) => {
  return l.every(num => num < t)
}

console.log(belowThreshold([1, 2, 4, 10], 100)) // true
console.log(belowThreshold([1, 20, 4, 10], 5)) // false

// The use of the .every() method in the given solution simplifies the function by eliminating the need for a loop and if statement.
// It will return true if all elements in the array pass the test (in this case, are less than t). If any element does not pass, it will return false.

// This solution is more efficient and readable than the original one.
// It's also a good practice to use built-in methods like .every() whenever possible, as they are usually more efficient and easier to read.

// This solution is also more maintainable. If the built-in method .every() is not supported in some JavaScript environments, you can replace it with a for loop and if statement.
// However, the built-in method is more likely to work correctly and is less likely to lead to bugs.

// Overall, this solution is a good example of how to write clean, efficient, and maintainable JavaScript code.

// You can also use the .some() method to solve this problem. The .some() method tests whether at least one element in the array passes the test implemented by the provided function.
// If it finds an element that passes the test, it returns true. Otherwise, it returns false.

const belowThreshold = (l, t) => {
  return !l.some(num => num >= t)
}

console.log(belowThreshold([1, 2, 4, 10], 100