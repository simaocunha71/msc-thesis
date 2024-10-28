```javascript
function list_sort(lst) {
  return lst.filter(str => str.length % 2 === 0).sort((a, b) => {
    if (a.length === b.length) {
      return a.localeCompare(b);
    }
    return a.length - b.length;
  });
}
```


Explanation:
The function list_sort takes a list of strings as a parameter. It uses the filter method to remove the strings that have odd lengths from the list. It then uses the sort method to sort the resulted list. The sort function is given a callback function that compares two strings. If the lengths of the two strings are the same, it compares them alphabetically. If the lengths are different, it sorts by the length. The result is a list of strings that have even lengths, sorted by the length and then alphabetically. The function returns this list.