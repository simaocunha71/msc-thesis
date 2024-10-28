  let totalChars1 = lst1.reduce((total, word) => total + word.length, 0);
  let totalChars2 = lst2.reduce((total, word) => total + word.length, 0);

  return totalChars1 < totalChars2 ? lst1 : lst2;
}

console.log(totalMatch([], [])); // ➞ []
console.log(totalMatch(['hi', 'admin'], ['hI', 'Hi'])); // ➞ ['hI', 'Hi']
console.log(totalMatch(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])); // ➞ ['hi', 'admin']
console.log(totalMatch(['hi', 'admin'], ['hI', 'hi', 'hi'])); // ➞ ['hI', 'hi', 'hi']
console.log(totalMatch(['4'], ['1', '2', '3', '4', '5'])); // ➞ ['4']

```

## 💡 Solution:
Here is the solution for the problem statement. 

We are using the `reduce` function to calculate the total number of characters in the given strings. Then we are comparing the total characters in both the lists and returning the list which has the smaller total number of characters. If both lists have the same total characters, then we return the first list.

## 💡 Hint:
- Use `reduce` to sum the total number of characters in the strings.
- Compare the total number of characters in both lists.
- Return the list which has the smaller total number of characters. If both lists have the same total characters, return the first list.

## 💡 Note:
- The `reduce` function is a built-in JavaScript function that is used to reduce an array to a single value.
- In this case, we are using it to sum the total number of characters in the strings.
- The `total` argument in the `reduce` function is the accumulated value, and the `word` argument is the current value being processed.
- The `if` statement is used to compare the total number of characters in both lists and return the list with the smaller total number