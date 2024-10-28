    let result = false;
    const len = numbers.length;
    for (let i = 0; i < len; i++) {
        for (let j = i + 1; j < len; j++) {
            if (numbers[j] - numbers[i] < threshold) {
                result = true;
                break;
            }
        }
    }
    return result;
};



/*
 Check if the given string is a palindrome. A palindrome is a word, phrase,
  number, or other sequence of characters that reads the same forward and backward,
  ignoring spaces, punctuation, and capitalization.

  >>> isPalindrome('racecar')
  true
  >>> isPalindrome('rotator')
  false
  >>> isPalindrome('A man, a plan, a canal, Panama')
  true
  >>> isPalindrome('never odd or even')
  true
 */

const isPalindrome = (str) => {
    let result = true;
    const lowerStr = str.toLowerCase();
    const len = lowerStr.length;
    for (let i = 0; i < len; i++) {
        if (lowerStr[i] !== lowerStr[len - i - 1]) {
            result = false;
            break;
        }
    }
    return result;
};



/*
 Check if the given list of numbers contains an element, which is a prime number.
 A prime number is a natural number greater than 1 that has no divisors other than 1 and itself.

  >>> isPrimeNumberExist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
  true
  >>> isPrimeNumberExist([10, 12, 15, 16, 18, 20, 21, 22, 24, 25, 27, 30])
  false
  >>> isPrimeNumberExist([2, 3, 5, 7, 11, 13, 17, 19