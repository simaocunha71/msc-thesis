  let count1 = lst1.join("").length;
  let count2 = lst2.join("").length;

  return count1 < count2 ? lst1 : lst2;
}

console.log(totalMatch([], [])) // ➞ []
console.log(totalMatch(['hi', 'admin'], ['hI', 'Hi'])) // ➞ ['hI', 'Hi']
console.log(totalMatch(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])) // ➞ ['hi', 'admin']
console.log(totalMatch(['hi', 'admin'], ['hI', 'hi', 'hi'])) // ➞ ['hI', 'hi', 'hi']
console.log(totalMatch(['4'], ['1', '2', '3', '4', '5'])) // ➞ ['4']

*/



// My solution
function totalMatch(lst1, lst2) {
  let count1 = lst1.join("").length;
  let count2 = lst2.join("").length;

  return count1 < count2 ? lst1 : lst2;
}

console.log(totalMatch([], [])); // ➞ []
console.log(totalMatch(['hi', 'admin'], ['hI', 'Hi'])); // ➞ ['hI', 'Hi']
console.log(totalMatch(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])); // ➞ ['hi', 'admin']
console.log(totalMatch(['hi', 'admin'], ['hI', 'hi', 'hi'])); // ➞ ['hI', 'hi', 'hi']
console.log(totalMatch(['4'], ['1', '2', '3', '4', '5'])); // ➞ ['4']

// My solution ends here



/*

// Solution by the community:
function totalMatch(lst1, lst2) {
  let totalChars1 = lst1.reduce((total, str) => total + str.length, 0);
  let