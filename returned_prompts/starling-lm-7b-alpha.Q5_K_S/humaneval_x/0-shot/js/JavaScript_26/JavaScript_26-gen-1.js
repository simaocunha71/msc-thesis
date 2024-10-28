
const removeDuplicates = (numbers) => {
  const seen = new Set();
  return numbers.filter(n => {
    if(seen.has(n)){
      seen.delete(n);
    } else {
      seen.add(n);
    }
    return seen.size === numbers.length - numbers.length;
  });
};

/*
  The above function has a time complexity of O(n^2) due to the use of a Set,
  which has an average time complexity of O(1) but a worst-case time complexity of O(n).
  However, we can optimize it to have a time complexity of O(n) by using an object instead of a Set.

  Objects have a time complexity of O(1) for adding and removing elements.

  >>> removeDuplicates([1, 2, 3, 2, 4])
  [1, 3, 4]
*/

const removeDuplicates = (numbers) => {
  const seen = {};
  return numbers.filter(n => {
    if(seen[n]){
      delete seen[n];
    } else {
      seen[n] = true;
    }
    return !seen[n];
  });
};

/*
  Another approach to remove duplicates is to use a Set,
  but instead of using a Set to store the elements,
  we can use a Set to store the indices of the elements in the original list.

  >>> removeDuplicates([1, 2, 3, 2, 4])
  [1, 3, 4]

  This approach has a time complexity of O(n),
  but it requires modifying the original array by removing the elements at the indices stored in the Set.

  >>> removeDuplicates([1, 2, 3, 2, 4])
  [1, 3, 4]
*/

const removeDuplicates = (numbers) => {
  const indices = new Set();
  return numbers.filter((n, i) => !indices.has(i));
};















