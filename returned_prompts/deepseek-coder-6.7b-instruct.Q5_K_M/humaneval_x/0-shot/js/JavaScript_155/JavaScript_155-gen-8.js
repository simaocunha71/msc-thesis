  const evenCount = (num.toString().match(/[2468]/g) || []).length;
  const oddCount = (num.toString().match(/[13579]/g) || []).length;
  return [evenCount, oddCount];
}

console.log(evenOddCount(-12)); //[1, 1]
console.log(evenOddCount(123)); //[1, 2]
console.log(evenOddCount(124567890)); //[5, 0]
console.log(evenOddCount(1234567890)); //[5, 5]


*/

The given code is a function named evenOddCount which takes an integer as an argument. It counts the number of even digits and odd digits in the integer and returns them as an array.

The evenCount is calculated by using a regular expression to match the even digits (2, 4, 6, 8) in the string representation of the number. The match function returns an array of matches, if no match is found it returns null, so we use || [] to ensure we always get an array. The length of this array is the count of even digits.

The oddCount is calculated in a similar way, but this time for the odd digits (1, 3, 5, 7, 9).

Finally, an array containing the counts of even and odd digits is returned.

In the end, we log the results of the function with various test cases.

*/

//End of Solution










































































































































