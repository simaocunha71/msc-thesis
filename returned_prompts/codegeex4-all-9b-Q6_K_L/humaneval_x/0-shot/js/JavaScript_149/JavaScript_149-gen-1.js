You can solve this problem by using the `filter` method to remove words with an odd length, and then use the `sort` method to sort the list alphabetically. Here's how you could do it:

```javascript
const sortedListSum = (lst) => {
  return lst.filter(word => word.length % 2 === 0).sort();
};
```

In this code, the `filter` method creates a new array with all elements that pass the test implemented by the provided function. The test function `word => word.length % 2 === 0` checks if the length of the word is even.

Then, the `sort` method sorts the elements of an array in place and returns the array. The default sort order is built upon converting the elements into strings, then comparing their sequences of UTF-16 code unit values.

So, the function will return a list of strings with even length, sorted in alphabetical order.