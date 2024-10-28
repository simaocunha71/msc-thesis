  const totalChars = lst ⇒ lst.reduce((acc, curr) ⇒ acc + curr.length, 0);

  return totalChars(lst1) < totalChars(lst2) ? lst1 : lst2;
}

// Test cases
console.log(totalMatch([], [])) // ➞ []
console.log(totalMatch(['hi', 'admin'], ['hI', 'Hi'])) // ➞ ['hI', 'Hi']
console.log(totalMatch(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])) // ➞ ['hi', 'admin']
console.log(totalMatch(['hi', 'admin'], ['hI', 'hi', 'hi'])) // ➞ ['hI', 'hi', 'hi']
console.log(totalMatch(['4'], ['1', '2', '3', '4', '5'])) // ➞ ['4']

/*
  This function first defines a helper function, totalChars, that calculates the total
  number of characters in a list of strings. It then uses this to get the total number
  of characters in both lists and compares these numbers. It returns the list with the
  smaller total number of characters. If the lists have the same number of characters,
  the function returns the first list.
  */


*/

// Test cases
console.log(totalMatch([], [])) // ➞ []
console.log(totalMatch(['hi', 'admin'], ['hI', 'Hi'])) // ➞ ['hI', 'Hi']
console.log(totalMatch(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])) // ➞ ['hi', 'admin']
console.log(totalMatch(['hi', 'admin'], ['hI', 'hi', 'hi'])) // ➞ ['hI', 'hi', 'hi']
console.log(totalMatch(['4'], ['1', '2', '3', '4', '5'])) // ➞ ['4']

/*
  This function first defines a helper function, totalChars, that