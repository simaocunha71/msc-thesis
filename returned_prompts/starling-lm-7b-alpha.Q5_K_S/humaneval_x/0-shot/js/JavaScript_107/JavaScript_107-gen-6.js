Even Count = 0;
Odd Count = 0;
for (let i = 1; i <= n; i++) {
  let str = i.toString();
  if (str === str.split('').reverse().join('')) {
    if (i % 2 === 0) {
      Even Count++;
    } else {
      Odd Count++;
    }
  }
}
return [Even Count, Odd Count];
};


/*
Explanation:

The idea here is to first initialize two counters, one for even and one for odd palindromes, as 0.
We then loop through all the integers between 1 and n (inclusive). For each integer, we first convert it to a string (since we need to reverse the string), and then check if the original string and the reversed string are the same. If they are the same, this means the integer is a palindrome.
Next, we check if the integer is even or odd. If it is even, we increment the even palindrome counter, otherwise, we increment the odd palindrome counter.
Finally, we return an array with the two counters as the result.

The time complexity of this function is O(n) as we only loop through the range from 1 to n once. The space complexity is O(1) as we only use a constant amount of space to store the two counters.

*/





























































































































































































