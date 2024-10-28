function totalMatch(lst1, lst2) {
    const total1 = lst1.reduce((acc, curr) => acc + curr.length, 0);
    const total2 = lst2.reduce((acc, curr) => acc + curr.length, 0);
    return total1 < total2 ? lst1 : lst2;
}

/*
  The function totalMatch takes two arrays (lists) of strings and returns
  the array (list) with total number of chars in the all strings of the array
  less than the other array. If the two arrays have the same number of chars,
  the first array is returned.

  The function uses the reduce method to add up the lengths of all strings
  in an array and stores the result in the total1 and total2 variables.

  The function then compares the total1 and total2 variables and returns
  the array with the lower total number of chars.
*/

*/

console.log(totalMatch([], []))  // [], []
console.log(totalMatch(['hi', 'admin'], ['hI', 'Hi']))  // ['hI', 'Hi']
console.log(totalMatch(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))  // ['hi', 'admin']
console.log(totalMatch(['hi', 'admin'], ['hI', 'hi', 'hi']))  // ['hI', 'hi', 'hi']
console.log(totalMatch(['4'], ['1', '2', '3', '4', '5']))  // ['4']




















































































































































