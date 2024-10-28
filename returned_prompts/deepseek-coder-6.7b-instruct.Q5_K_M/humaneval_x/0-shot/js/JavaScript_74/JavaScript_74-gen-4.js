  let sum1 = lst1.join('').length;
  let sum2 = lst2.join('').length;

  return sum1 < sum2 ? lst1 : lst2;
}

console.log(totalMatch([], [])); // ➞ []
console.log(totalMatch(['hi', 'admin'], ['hI', 'Hi'])); // ➞ ['hI', 'Hi']
console.log(totalMatch(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])); // ➞ ['hi', 'admin']
console.log(totalMatch(['hi', 'admin'], ['hI', 'hi', 'hi'])); // ➞ ['hI', 'hi', 'hi']
console.log(totalMatch(['4'], ['1', '2', '3', '4', '5'])); // ➞ ['4']

This function first calculates the total number of characters in both lists by joining the lists into a single string with no separators, and then getting the length of that string. It then returns the list that has a smaller total character count. If the two counts are equal, it returns the first list.
*/

function totalMatch(lst1, lst2) {
  let sum1 = lst1.join('').length;
  let sum2 = lst2.join('').length;

  return sum1 < sum2 ? lst1 : lst2;
}

console.log(totalMatch([], [])); // ➞ []
console.log(totalMatch(['hi', 'admin'], ['hI', 'Hi'])); // ➞ ['hI', 'Hi']
console.log(totalMatch(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])); // ➞ ['hi', 'admin']
console.log(totalMatch(['hi', 'admin'], ['hI', 'hi', 'hi'])); // ➞ ['hI', 'hi', 'hi']
console.log(totalMatch(['4'], ['1', '2', '3', '4', '5'])); // ➞ ['4']

/*
Test.assertEquals(totalMatch([