    let stack = [];
    for (let i = 0; i < string.length; i++) {
        if (string[i] == '[') {
            stack.push(string[i]);
        } else if (string[i] == ']' && stack.length > 0) {
            stack.pop();
        }
    }

    return stack.length > 0;
};


/*
  Create a function that takes a string as input which contains only square brackets.
  The function should return true if and only if there is a valid subsequence of brackets
  where at least one bracket in the subsequence is nested.
  isNested('[[]]') ➞ true
  isNested('[]]]]]]][[[[[]') ➞ false
  isNested('[][]') ➞ false
  isNested('[]') ➞ false
  isNested('[[][]]') ➞ true
  isNested('[[]][[') ➞ true
  isNested('[[]][[') ➞ true
  */


/*
  Create a function that takes an array of numbers as an argument and returns the average of all the numbers in the array.
  average([2, 3, 5, 6]) ➞ 4
  average([1, 3, 5, 6, 9, 10]) ➞ 6.333333333333333
  average([3, 5, 8, 10]) ➞ 7.25
  average([1, 2, 3, 4, 5]) ➞ 3
  average([]) ➞ 0
  */

const average = (nums) => {
    return nums.reduce((a, b) => a + b, 0) / nums.length;
};



/*
  Create a function called `capitalize` that takes a string as an argument and returns a new string where the first
  letter of each word is capitalized and all other letters are lowercase.