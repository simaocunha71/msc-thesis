  const seen = {};
  for (let i = 0; i < string.length; i++) {
    const char = string[i];
    if (seen[char]) {
      continue;
    }
    seen[char] = true;
  }
  return Object.keys(seen).length;
};

countDistinctCharacters('xyzXYZ'); // 3
countDistinctCharacters('Jerry'); // 4

*/






/*
  >>> kthSmallest([3, 5, 1, 8, 2], 3)
  1
  >>> kthSmallest([3, 5, 1, 8, 2], 5)
  3
  >>> kthSmallest([3, 5, 1, 8, 2], 2)
  5
  >>> kthSmallest([3, 5, 1, 8, 2], 4)
  8
  >>> kthSmallest([3, 5, 1, 8, 2], 6)
  undefined

  Given an array of numbers, find the kth smallest number in it. Return undefined if the array does not contain the kth smallest number.

  Note that the array may contain duplicates or negative numbers, and k is 1-indexed.
*/

const kthSmallest = (arr, k) => {
  arr.sort((a, b) => a - b);
  return arr[k - 1];
};

kthSmallest([3, 5, 1, 8, 2], 3); // 1
kthSmallest([3, 5, 1, 8, 2], 5); // 3
kthSmallest([3, 5, 1, 8, 2], 2); // 5
kthSmallest([3, 5, 1, 8, 2], 4); // 8
kthSmallest([3, 5, 1, 8, 2], 6); // undefined




/*
  >>> longestWord('I love coding')
  'coding'
  >>> longestWord