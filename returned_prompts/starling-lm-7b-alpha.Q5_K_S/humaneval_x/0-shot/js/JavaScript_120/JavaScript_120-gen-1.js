  let res = [];
  let max = -Infinity;
  let counter = 0;

  arr.sort((a, b) => b - a);

  while (counter < k && arr.length > 0) {
    res.push(arr.shift());
    counter++;
  }

  return res;
};

console.log(maximum([-3, -4, 5], 3)); // [-4, -3, 5]
console.log(maximum([4, -4, 4], 2)); // [4, 4]
console.log(maximum([-3, 2, 1, 2, -1, -2, 1], 1)); // [2]

*/

