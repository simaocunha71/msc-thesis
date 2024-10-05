```
const sortArray = (arr) => {
  return arr.sort((a, b) => {
    if (a.toString(2).split('1').length - b.toString(2).split('1').length !== 0) {
      return a.toString(2).split('1').length - b.toString(2).split('1').length;
    } else {
      return a - b;
    }
  });
};
```


Explanation:
The sort function is used to sort the array. The callback function is used to determine the sort order.
The callback function is called with two arguments, `a` and `b`, which are the elements being compared.
We first convert the numbers to binary strings using `toString(2)` and then split the strings into arrays using `split('1')`. The length of these arrays is the number of ones in the binary representation of the numbers.
If the number of ones is different, we return the difference. If the number of ones is the same, we return the difference between the numbers themselves. This ensures that numbers with the same number of ones are sorted in ascending order.