return l.every((curr, index, arr) => {
  return index === 0 || curr >= arr[index - 1];
});
};

/*Return true if a string is a palindrome
  >>> isPalindrome('racecar')
  true
  >>> isPalindrome('rotator')
  false
  >>> isPalindrome('level')
  true
  */
const isPalindrome = (s) => {
  return s === s.split('').reverse().join('');
};

/*Return all possible subsets of the array.
  >>> subsets([1, 2, 3])
  [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
  >>> subsets(['a', 'b', 'c'])
  [[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
  */
const subsets = (a) => {
  return [[]].concat(
    a.reduce(
      (acc, val, i) =>
        acc.concat(
          acc.map((set) => set.concat(val)).filter((set) => !set.includes(val)),
        ),
      [[]],
    ),
  );
};

// Export these functions so they can be tested.
module.exports = {
  monotonic,
  isPalindrome,
  subsets,
};
















































































































































