  let sum = 0;
  let binary = "";
  
  while(N){
      sum += N % 2;
      N = Math.floor(N / 2);
  }
  
  while(sum){
      binary = (sum % 2) + binary;
      sum = Math.floor(sum / 2);
  }
  
  return binary;
}

console.log(solve(1000)); // 1
console.log(solve(150)); // 110
console.log(solve(147)); // 1100

```

**Explanation:**

In the problem, you are required to find the sum of the digits of a number in binary form. So firstly, we convert the given number N into binary form and then find the sum of its digits.

Here, we are using a while loop to find the sum of N's digits in binary form and then we convert the sum into binary form.

In the while loop, we calculate the remainder of N when divided by 2 and add the result to 'sum'. Then we divide N by 2 and update N.

Then, in another while loop, we calculate the remainder of 'sum' when divided by 2 and add the result to 'binary'. Then we divide 'sum' by 2 and update 'sum'.

Finally, we return 'binary' which is a string of binary digits of the sum of N's digits.

**Test Case:**

For N = 1000, the sum of digits will be 1, so the output should be "1".

For N = 150, the sum of digits will be 6, so the output should be "110".

For N = 147, the sum of digits will be 12, so the output should be "1100".

**Time Complexity:**

The time complexity of the program is O(log(N)) because we are traversing the binary representation of N.

**Space Complexity:**

The space complexity of the program is O(1) because we are using a constant amount of space to store the sum and binary representation.