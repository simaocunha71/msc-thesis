  let count = 0;
  let position = 0;

  // Loop through the string
  while (true) {
    position = string.indexOf(substring, position);
    if (position === -1) break;
    count++;
    position++;
  }

  return count;
}

console.log(howManyTimes('', 'a')) // 0
console.log(howManyTimes('aaa', 'a')) // 3
console.log(howManyTimes('aaaa', 'aa')) // 3


// The function works by using the indexOf method, which returns the position of the first occurrence of a specified value in a string.
// When it finds a match, it increments the count and moves the position to the next character.
// The loop continues until indexOf returns -1, which means there are no more occurrences of the substring in the string.
// Finally, it returns the count.
// The function is case-sensitive, so 'a' and 'A' are different characters.
// If you want to make it case-insensitive, you can convert both the string and substring to lower case inside the function.

```

**Explanation:**

In the code provided, we are defining a function `howManyTimes` that takes two parameters: `string` and `substring`. 

We initialize a variable `count` to 0, which will keep track of the number of times `substring` appears in `string`.

We also initialize a variable `position` to 0, which will keep track of the current position in `string` where we are looking for `substring`.

We then enter a while loop that continues until `indexOf` returns -1, indicating that `substring` is no longer found in `string` starting at the current `position`.

Inside the loop, `indexOf` is called with the current `position` as the second argument, to find the next occurrence of `substring` in `string`. If `indexOf` returns -1, the loop breaks. Otherwise, `count` is incremented and `position` is set to the next character after the found occurrence.

Finally, the function returns `count`, which is the total number of times `substring