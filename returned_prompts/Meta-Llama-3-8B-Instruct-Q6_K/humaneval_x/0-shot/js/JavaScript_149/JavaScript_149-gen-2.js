```javascript
const sortedListSum = (lst) => {
  const filteredList = lst.filter(word => word.length % 2 === 0);
  return filteredList.sort((a, b) => {
    if (a.length === b.length) {
      return a.localeCompare(b);
    }
    return a.length - b.length;
  });
};
```


Explanation:
The function `sortedListSum` takes a list of strings as input and returns a sorted list of strings. 

First, it filters out the strings that have odd lengths from the list using the `filter` method. The callback function `word => word.length % 2 === 0` returns a boolean indicating whether the word has an even length. If the word has an even length, it is included in the resulting list; otherwise, it is excluded.

Then, it sorts the filtered list using the `sort` method. The callback function `(a, b) => ...` defines the comparison logic. It first checks if the lengths of the two words are equal. If they are, it sorts the words alphabetically using `a.localeCompare(b)`. If the lengths are not equal, it sorts the words by their lengths using `a.length - b.length`.

The `localeCompare` method is used to compare the words alphabetically. It returns a negative value if `a` comes before `b`, a positive value if `a` comes after `b`, and 0 if `a` and `b` are equal.

Finally, the sorted list is returned. If the input list is `["aa", "a", "aaa"]`, the function will return `["aa"]`. If the input list is `["ab", "a", "aaa", "cd"]`, the function will return `["ab", "cd"]`. 