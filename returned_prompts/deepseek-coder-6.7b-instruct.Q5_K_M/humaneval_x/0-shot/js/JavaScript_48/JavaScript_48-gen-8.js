  let reversed = text.split('').reverse().join('');
  return text === reversed;
};

// Tests
console.log(isPalindrome('')); // true
console.log(isPalindrome('aba')); // true
console.log(isPalindrome('aaaaa')); // true
console.log(isPalindrome('zbcd')); // false

// Explanation
// This function takes a string as input and checks if it's a palindrome. 
// A palindrome is a word, number, phrase, or other sequences of characters that reads the same forward and backward, 
// ignoring spaces, punctuation, and capitalization. 
// The function splits the string into an array of characters, reverses it, and joins it back together. 
// If the original string and the reversed string are the same, the function returns true, indicating that the string is a palindrome. 
// Otherwise, it returns false.

// Note: This function assumes that the input is a string. If the input is not a string, the function may not behave as expected.

// This function has a time complexity of O(n), where n is the length of the string. This is because it splits the string into an array of characters in O(n) time, reverses the array in O(n) time, and joins the array back into a string in O(n) time. 
// The space complexity is also O(n), as it creates a new array of characters to store the reversed string.

// This function is case sensitive and does not ignore spaces or punctuation. If you want to make it case insensitive, you can add .toLowerCase() to both the text and reversed variables. 
// If you want to ignore spaces, punctuation, and capitalization, you can use a regular expression to remove them from the text and reversed variables.

// You can also use two pointers technique to solve this problem in O(n) time complexity and O(1) space complexity.

// This function can be used in any programming language that supports string manipulation and array methods.
// It's also a good example of how to use higher-order functions like split, reverse, and join in JavaScript.
// Enjoy coding :)
