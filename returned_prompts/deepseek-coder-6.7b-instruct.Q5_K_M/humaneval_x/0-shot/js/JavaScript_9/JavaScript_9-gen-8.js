  let max = -Infinity;
  return numbers.map(n => (max = Math.max(n, max)));
};

console.log(rollingMax([1, 2, 3, 2, 3, 4, 2])); // [1, 2, 3, 3, 3, 4, 4]

*/

