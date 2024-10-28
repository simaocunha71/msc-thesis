  let even_palindrome = 0;
  let odd_palindrome = 0;

  for (let i = 1; i <= n; i++) {
    if (is_palindrome(i) && is_even(i)) {
      even_palindrome += 1;
    }
    if (is_palindrome(i) && is_odd(i)) {
      odd_palindrome += 1;
    }
  }

  return [even_palindrome, odd_palindrome];
}

// Helper Functions

// Check if a number is even
const is_even = (num) => {
  return num % 2 === 0;
}

// Check if a number is odd
const is_odd = (num) => {
  return num % 2 !== 0;
}

// Check if a number is a palindrome
const is_palindrome = (num) => {
  return num.toString() === num.toString().split('').reverse().join('');
}
