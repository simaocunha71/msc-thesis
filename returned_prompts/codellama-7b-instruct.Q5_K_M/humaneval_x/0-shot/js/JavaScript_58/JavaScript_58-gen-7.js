/*Return sorted unique common elements for two lists.
  >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
  [1, 5, 653]
  >>> common([5, 3, 2, 8], [3, 2])
  [2, 3]

  */
const common = (l1, l2) => {
  // TODO: Write your code here
  const a = [...new Set(l1)].sort((a, b) => a - b);
  const b = [...new Set(l2)].sort((a, b) => a - b);
  const common = [];

  for (let i = 0; i < a.length; i++) {
    for (let j = 0; j < b.length; j++) {
      if (a[i] === b[j]) {
        common.push(a[i]);
      }
    }
  }

  return common;
};

// Tests
const assert = require('assert');

assert.deepEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [
  1,
  5,
  653,
]);

assert.deepEqual(common([5, 3, 2, 8], [3, 2]), [2, 3]);

assert.deepEqual(common([1, 2, 3, 4, 5], [10, 20, 30, 40, 50]), []);

assert.deepEqual(common([], [1, 2, 3]), []);

assert.deepEqual(common([1, 2, 3], []), []);

assert.deepEqual(common([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),