  if (arr.length === 0) return true;
  let shifted = [...arr];
  for (let i = 0; i < arr.length; i++) {
    shifted.unshift(shifted.pop());
    if (isSorted(shifted)) return true;
  }
  return false;
};

const isSorted = (arr) => {
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] > arr[i + 1]) return false;
  }
  return true;
};

console.log(moveOneBall([3, 4, 5, 1, 2])); // true
console.log(moveOneBall([3, 5, 4, 1, 2])); // false

// The time complexity of the solution is O(n^2) as we are doing a shift operation n times and for each shift operation, we are checking if the array is sorted or not.
// The space complexity of the solution is O(n) as we are creating a copy of the array for each shift operation.

// Here, 'n' is the size of the array.

// The solution works by performing a right shift operation on the array and checking if the array becomes sorted after each shift operation. If after performing any number of shift operations, the array becomes sorted, we return true. If we don't find any such shift operation, we return false.

// The isSorted function is used to check if the array is sorted in non-decreasing order. It iterates over the array and checks if each element is less than or equal to the next element. If it is, it returns true. If it finds any element that is greater than the next one, it returns false.

// The moveOneBall function creates a copy of the array and performs a right shift operation on it. It then checks if the array is sorted. If it is, it returns true. If it is not, it repeats the process until it has shifted the array n times or it finds an array that is sorted.

// The time complexity of the solution is O(n^2) because of the nested loop. The outer loop runs n times and for each iteration of the outer loop