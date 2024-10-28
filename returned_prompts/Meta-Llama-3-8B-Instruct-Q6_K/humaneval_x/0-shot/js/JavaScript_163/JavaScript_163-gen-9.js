```
const generateIntegers = (a, b) => {
  if (a > b) [a, b] = [b, a]; // ensure a is smaller than b
  let result = [];
  for (let i = a; i <= b; i++) {
    let str = i.toString();
    for (let j = 0; j < str.length; j++) {
      if (+str[j] % 2 === 0) result.push(+str[j]);
    }
  }
  return result;
};
```


Explanation:
The function `generateIntegers` takes two positive integers `a` and `b` as input, and returns an array of even digits between `a` and `b`, in ascending order.

First, we ensure that `a` is smaller than `b` by swapping them if necessary.

Then, we initialize an empty array `result` to store the even digits.

We use two nested loops to iterate through each digit of each integer between `a` and `b`. The outer loop iterates through each integer, and the inner loop iterates through each digit of the integer.

For each digit, we check if it is even by using the modulo operator (`%`). If the remainder is 0, it means the digit is even, so we add it to the `result` array.

Finally, we return the `result` array, which contains all the even digits between `a` and `b`, in ascending order.

The time complexity of this function is O((b-a+1)*log(b)), where `log(b)` is the time complexity of converting an integer to a string, and `O((b-a+1))` is the time complexity of the two nested loops. The space complexity is O(b-a+1), which is the maximum size of the `result` array.