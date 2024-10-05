  const checkDigit = (num) => {
    const strNum = num.toString();
    for (let i = 0; i < strNum.length; i++) {
      if (strNum[i] % 2 === 0) {
        return false;
      }
    }
    return true;
  }

  const result = [];
  for (let i = 0; i < x.length; i++) {
    if (checkDigit(x[i])) {
      result.push(x[i]);
    }
  }
  
  return result.sort((a, b) => a - b);
}

console.log(uniqueDigits([15, 33, 1422, 1]));
console.log(uniqueDigits([152, 323, 1422, 10]));

// Output:
// [1, 15, 33]
// []
```

This function `uniqueDigits` takes a list of positive integers and returns a sorted list of all elements that have no even digits. Firstly, it defines a helper function `checkDigit` that takes a number and checks if any digit in this number is even. If it is, the function returns `false`, otherwise it returns `true`.

Then it creates an empty list `result` and goes through each number in the input list. If `checkDigit` returns `true` for a number, it adds this number to `result`.

Finally, it returns `result` sorted in increasing order.

The time complexity of this function is O(n*m), where n is the number of elements in the input list and m is the average number of digits in these numbers.

The space complexity of this function is O(n), where n is the number of elements in the input list.
*/
```















































































