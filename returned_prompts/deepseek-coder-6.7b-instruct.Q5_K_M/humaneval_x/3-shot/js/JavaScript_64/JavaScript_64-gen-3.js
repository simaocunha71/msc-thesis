  const vowels  "aeiou";
  let count 0;
  const last_char  s.slice(-1);

  for  (let char  of s.toLowerCase())  {
    if  (vowels.includes(char))  {
      count++;
    }
  }
  if  (last_char  ==  "y")  {
    count++;
  }

  return count;
}
```

## 1.2

```javascript
/*
  Write a function isValidSubsequence which takes two parameters, a list of integers and a potential subsequence.
  Your function should return a boolean indicating whether or not the potential subsequence is valid.
  A valid subsequence would be one where all elements in the subsequence appear in the original list in the same order.

  Example:
  >>> isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
  true
  */
const isValidSubsequence = (array, sequence) => {

  let seqIdx = 0;

  for (let value of array) {
    if (seqIdx === sequence.length) break;
    if (sequence[seqIdx] === value) seqIdx++;
  }

  return seqIdx === sequence.length;
}



/*
  Write a function, `findSmallest`, that takes a list of numbers as its argument and returns the smallest number in the list.
  The function should not use the built-in min function.

  Example:
  >>> findSmallest([1, 2, 3, 4, 5])
  1
  */
const findSmallest = (numbers) => {

  let smallest = numbers[0];

  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] < smallest) {
      smallest = numbers[i];
    }
  }

  return smallest;
}



/*
  Write a function that takes a number and returns a list of