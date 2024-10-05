  // check if empty
  if (!arr.length) return [];

  // check if only one element
  if (arr.length === 1) return [arr[0], 0];

  // check if only two elements
  if (arr.length === 2) {
    const [a, b] = arr;
    return (a % 2 === 0 && b % 2 === 0) ? [a, 0] : [b, 1];
  }

  // check if more than two elements

  const evens = arr.filter((_, i) => arr[i] % 2 === 0);

  // if there are no evens, return null
  if (!evens.length) return [];

  // find the smallest even
  const smallest = evens.reduce((acc, cur) => {
    if (cur < acc) return cur;
    return acc;
  }, evens[0]);

  // find the index of the smallest
  const smallestIndex = evens.findIndex(n => n === smallest);

  return [smallest, smallestIndex];
};

const testCases = [
  [4, 2, 3],
  [1, 2, 3],
  [],
  [5, 0, 3, 0, 4, 2],
];

for (let i = 0; i < testCases.length; i++) {
  const testCase = testCases[i];
  console.log(pluck(testCase));
}
