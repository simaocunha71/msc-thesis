/*Return sorted unique common elements for two lists.
  >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
  [1, 5, 653]
  >>> common([5, 3, 2, 8], [3, 2])
  [2, 3]

  */
const common = (l1, l2) => {
  const sortedL1 = sort(l1);
  const sortedL2 = sort(l2);
  // remove duplicate elements from both lists
  // and store the remaining
  const result = [];

  for (let i = 0; i < sortedL1.length && i < sortedL2.length; i++) {
    if (!sortedL1[i] || !sortedL2[i]) continue;
    else if (result.indexOf(sortedL1[i]) == -1) result.push(sortedL1[i]);
    else if (result.indexOf(sortedL2[i]) == -1) result.push(sortedL2[i]);
  }

  return result;
};

const sort = (arr) => {
  // base case: empty array, done!
  if (!Array.isArray(arr)) return arr;

  // sort ascendingly based on the index
  const sorted = arr.sort((a, b) => a - b);

  // return sorted version of the input list
  return sorted;
};
