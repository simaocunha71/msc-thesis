  let sum1 = lst1.reduce((a, b) => a + b.length, 0);
  let sum2 = lst2.reduce((a, b) => a + b.length, 0);
  return sum1 < sum2 ? lst1 : lst2;
}

console.log(totalMatch([], []))
console.log(totalMatch(['hi', 'admin'], ['hI', 'Hi']))
console.log(totalMatch(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))
console.log(totalMatch(['hi', 'admin'], ['hI', 'hi', 'hi']))
console.log(totalMatch(['4'], ['1', '2', '3', '4', '5']))

// The function totalMatch first calculates the sum of the lengths of all strings in lst1 and lst2 respectively. It then compares these sums and returns the list with the smaller sum. If the sums are equal, lst1 is returned.



// the reduce() method executes a reducer function on each element of the array, resulting in a single output value.
// In this case, the reducer function takes two arguments: the accumulator (a) and the current value (b). It adds the length of the current value to the accumulator and returns the result.
// The initial value of the accumulator is 0, because we're summing the lengths of the strings.
// The result is the total number of characters in all the strings in the list.
// The ternary operator (?) is used to return the appropriate list based on the comparison of the sums.
// If sum1 is less than sum2, lst1 is returned. Otherwise, lst2 is returned.

// This solution has a time complexity of O(n) because we have to iterate through each string in both lists once.
// The space complexity is O(1) because we only store the sums and the input lists.

// Note: This solution assumes that the input lists will always contain only strings. If this is not the case, you should add some error checking to handle non-string values.

// Also note that this solution is case-sensitive. If you want to ignore case when comparing the strings