    const primeNumber = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
    const num = primeNumber.find(number => a % number === 0);
    if (num) {
      return isMultiplyPrime(a / num);
    }
    return true;
};

/*
  Write a function that returns the first character of a given string.
  Example:
  getFirstChar('Hello') == 'H'
 */
const getFirstChar = (str) => {
    return str[0];
};

/*
  Write a function that returns the length of the string.
  Example:
  getLength('Hello') == 5
 */
const getLength = (str) => {
    return str.length;
};

/*
  Write a function that returns the index of the first occurrence of a given character in a string.
  If the character does not exist in the string, the function should return -1.
  Example:
  indexOfChar('Hello', 'o') == 3
 */
const indexOfChar = (str, char) => {
    const index = str.indexOf(char);
    return index === -1 ? -1 : index;
};

/*
  Write a function that takes a string and a character as parameters and returns a new string that replaces the first occurrence of the character with the given character.
  Example:
  replaceChar('Hello', 'o', 'e') == 'Helle'
 */
const replaceChar = (str, oldChar, newChar) => {
    const index = str.indexOf(oldChar);
    if (index === -1) {
        return str;
    }
    return str.slice(0, index) + newChar + str.slice(index + 1);
};

/*
  Write a function that takes a string and a character as parameters and