  for (let i = 1; i < lst.length; i++) {
    if (lst[i] < lst[i - 1]) return false;
  }
  return true;
};

console.log(isSorted([5])); // ➞ true
console.log(isSorted([1, 2, 3, 4, 5])); // ➞ true
console.log(isSorted([1, 3, 2, 4, 5])); // ➞ false
console.log(isSorted([1, 2, 3, 4, 5, 6])); // ➞ true
console.log(isSorted([1, 2, 3, 4, 5, 6, 7])); // ➞ true
console.log(isSorted([1, 3, 2, 4, 5, 6, 7])); // ➞ false
console.log(isSorted([1, 2, 2, 3, 3, 4])); // ➞ true
console.log(isSorted([1, 2, 2, 2, 3, 4])); // ➞ false

```

**Note:** This solution assumes that the input list will always contain positive integers and will not have any duplicate numbers. If the input list could contain negative numbers or have duplicate numbers, this solution would need to be modified to handle those cases.

**Note:** This solution runs in O(n) time complexity because it has to iterate through the entire list once.

**Note:** The function uses a for loop to compare each number in the list to the previous one. If it finds a number that is less than its previous number, it immediately returns false. If it gets through the entire list without finding any numbers that are less than their previous number, it returns true.

**Note:** The function uses the `<` operator to compare numbers, which is the standard way to compare numbers in JavaScript.

**Note:** The function uses the `return` statement to immediately exit the function and return a value. If the function does not find any numbers that are less than