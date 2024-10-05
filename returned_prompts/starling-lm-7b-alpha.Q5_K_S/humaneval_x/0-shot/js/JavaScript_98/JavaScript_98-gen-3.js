  let count = 0;
  const vowels = ['A', 'E', 'I', 'O', 'U'];

  for (let i = 0; i < s.length; i++) {
    if (vowels.includes(s[i].toUpperCase()) && i % 2 === 0) {
      count++;
    }
  }

  return count;
};

countUpper('aBCdEf');

/*
  The above code snippet defines a function called `countUpper` that accepts a string `s` as an argument. It initializes a variable `count` to 0, and a constant `vowels` that contains all uppercase vowels.

  The function uses a `for` loop to iterate over each character in the string `s`. Inside the loop, it checks if the current character is an uppercase vowel and if the index of the character is even. If both conditions are true, it increments the `count` variable by 1.

  Finally, the function returns the value of the `count` variable, which represents the number of uppercase vowels in even indices of the input string.

  In the example usage `countUpper('aBCdEf')`, the function is called with the string `'aBCdEf'`. The function counts the number of uppercase vowels in even indices of this string, which is 1 in this case.

  The function can be used to count the number of uppercase vowels in any given string by providing the string as an argument to the function.
*/





















































































































































