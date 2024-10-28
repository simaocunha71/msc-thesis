To solve this problem, you can follow these steps:

1. First, filter out all the odd length strings from the list. You can use the filter method to achieve this. This method will create a new array with all the strings that have an even length.

2. Next, sort the filtered array in ascending order by length of each word. You can use the sort method with a compare function to achieve this. In the compare function, first compare the lengths of the words. If the lengths are equal, then compare the alphabetical order of the words.

3. Finally, return the sorted array.

Here's an example of how you can implement this solution in JavaScript:

```javascript
const list_sort = (lst) => {
  const evenLengthStrings = lst.filter((str) => str.length % 2 === 0);
  evenLengthStrings.sort((a, b) => {
    if (a.length < b.length) {
      return -1;
    } else if (a.length > b.length) {
      return 1;
    } else {
      return a.localeCompare(b);
    }
  });
  return evenLengthStrings;
};
```

In this code, the filter method is used to create a new array `evenLengthStrings` that only contains the strings with an even length. The sort method is then used to sort the `evenLengthStrings` array in ascending order by length of each word. The compare function inside the sort method first compares the lengths of the words. If the lengths are equal, it compares the alphabetical order of the words using the `localeCompare` method.

You can then use this `list_sort` function to sort your list of strings as described in the problem statement.

Note: The `localeCompare` method is used for sorting the strings in alphabetical order in case of equal lengths. This method returns -1, 0, or 1 depending on whether the first string is less than, equal to, or greater than the second string, respectively.

Hope this helps! Let me know if you have any further questions.

Here is a test to verify the correctness of your implementation:

```javascript
assert list_sort(["aa", "a", "aaa