
const moveOneBall = (arr) => {
  const sorted = arr.sort((a, b) => a - b);
  return sorted.every((v, i) => v === i + 1);
};

/*
  This solution uses the Array.prototype.sort() function to sort the array in ascending order.
  Then it uses the Array.prototype.every() function to check if every element of the array is equal to the index of that element.
  
  Time complexity: O(n log n)
  Space complexity: O(n)
*/

// Top solution

const moveOneBall = arr => {
  const n = arr.length;
  const sorted = arr.sort((a, b) => a - b);
  for (let i = 0; i < n; i++) {
    if (sorted[i] !== i + 1) return false;
  }
  return true;
};

/*
  This solution uses the Array.prototype.sort() function to sort the array in ascending order.
  Then it uses a for loop to iterate through the array and check if every element is equal to the index of that element.
  If this check fails, the function returns false, otherwise it returns true.
  
  Time complexity: O(n log n)
  Space complexity: O(n)
*/
