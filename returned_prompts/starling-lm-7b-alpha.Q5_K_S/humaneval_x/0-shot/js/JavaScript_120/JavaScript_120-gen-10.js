    const len = arr.length;
    const sorted = arr.slice().sort((a, b) => b - a);
    return sorted.slice(0, k);
};

// Test
console.log(maximum([-3, -4, 5], 3)); // [-4, -3, 5]
console.log(maximum([4, -4, 4], 2)); // [4, 4]
console.log(maximum([-3, 2, 1, 2, -1, -2, 1], 1)); // [2]

*/

/*
  Given a string s and an integer k,
  return the k most frequent words in the string.
  Return them in descending order of frequency, sorted.

  Example 1:
      Input: s = "hereanthem", k = 2
      Output: ["here", "anthem"]

  Example 2:
      Input: s = "apple apple", k = 1
      Output: ["apple"]

  Note:
      1. You may assume k is always valid, meaning k is in the range [1, the number of unique
         characters in the input].

  Follow-up:
      Try to solve it in O(n + k) time complexity.


*/

const topKFrequent = function(words, k) {
    const map = {};
    for (let word of words) {
        map[word] = map[word] + 1 || 1;
    }

    const sorted = Object.keys(map).sort((a, b) => map[b] - map[a]);
    return sorted.slice(0, k);
};

















































































































