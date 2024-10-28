  const sumChars = lst ⇒ lst.reduce((total, word) ⇒ total + word.length, 0);
  return sumChars(lst1) < sumChars(lst2) ? lst1 : lst2;
}

Explanation:
  This solution works by creating a helper function, sumChars, that sums the lengths of all strings in a list.

  Then it uses a ternary operator to return lst1 if its total character count is less than that of lst2. Otherwise, it returns lst2.

  Note that JavaScript's reduce function is used to sum the lengths of all strings in the list.
*/

// test cases
console.log(totalMatch([], [])) // ➞ []
console.log(totalMatch(['hi', 'admin'], ['hI', 'Hi'])) // ➞ ['hI', 'Hi']
console.log(totalMatch(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])) // ➞ ['hi', 'admin']
console.log(totalMatch(['hi', 'admin'], ['hI', 'hi', 'hi'])) // ➞ ['hI', 'hi', 'hi']
console.log(totalMatch(['4'], ['1', '2', '3', '4', '5'])) // ➞ ['4']

/*
  This function works by summing the lengths of all strings in each list and comparing the results. If the sum of the lengths of the strings in the first list is less than the sum in the second list, it returns the first list. Otherwise, it returns the second list.
*/

```

## 3. Write a JavaScript function that takes an array of objects and a key, and returns a new array of objects with the key filtered out.

```javascript
