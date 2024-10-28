```javascript
const sortedListSum = (lst) => {
  let filteredList = lst.filter(word => word.length % 2 === 0);
  filteredList.sort((a, b) => {
    if (a.length === b.length) {
      return a.localeCompare(b);
    } else {
      return a.length - b.length;
    }
  });
  return filteredList;
};
```
Explanation:
The function `sortedListSum` takes a list of strings as a parameter. It filters out the strings that have odd lengths using the `filter` method. Then, it sorts the resulting list in ascending order based on the length of each string. If two strings have the same length, it sorts them alphabetically using the `localeCompare` method. Finally, it returns the sorted list.

The unit test `assert list_sort(["aa", "a", "aaa"]) => ["aa"]` helps to understand the problem better. It shows that the function should return a list of strings in sorted order, with strings of even length first, and then strings of odd length. If two strings have the same length, the function should sort them alphabetically.

The unit test `assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]` also helps to understand the problem better. It shows that the function should return a list of strings in sorted order, with strings of even length first, and then strings of odd length. If two strings have the same length, the function should sort them alphabetically. In this case, "ab" and "cd" have the same length, so they are sorted alphabetically.