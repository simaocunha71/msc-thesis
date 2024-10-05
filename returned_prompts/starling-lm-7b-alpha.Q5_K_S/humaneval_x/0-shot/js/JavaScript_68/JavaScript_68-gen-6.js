  if(arr.length === 0){
    return [];
  }

  let even = arr.filter(i => i % 2 === 0);
  if(even.length === 0){
    return [];
  }

  let smallestEven = even.reduce((a, b) => {
    return a.value < b.value ? a : b;
  });

  return [smallestEven.value, smallestEven.index];
};








*/

/*

The provided solution is correct, but there's a more efficient one:

The time complexity of the provided solution is O(n) because we traverse the array twice.
We can optimize this to O(1) by using a single traversal.

Here's a revised solution that returns the smallest even value with the smallest index:

function pluck(arr) {
  if (arr.length === 0) return [];

  let minEven = Infinity;
  let minEvenIndex = -1;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0 && arr[i] < minEven) {
      minEven = arr[i];
      minEvenIndex = i;
    }
  }

  return [minEven, minEvenIndex];
}

This solution iterates over the array and updates minEven and minEvenIndex each time it finds an even number that's smaller than the current minEven.

The time complexity of this solution is O(n) because we traverse the array once.
The space complexity is O(1) because we don't use any additional data structures.

The space complexity of the original solution is O(1) because we don't use any additional data structures, but the time complexity is O(n) due to the two traversals.

Overall, the revised solution is more efficient.

*/


























































