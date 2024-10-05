  let roman = '', i = 0;
  const map = [
    ['m', 1000], ['cm', 900], ['d', 500], ['cd', 400],
    ['c', 100], ['xc', 90], ['l', 50], ['xl', 40],
    ['x', 10], ['ix', 9], ['v', 5], ['iv', 4],
    ['i', 1]
  ];

  while (number > 0) {
    if (map[i][1] <= number) {
      roman += map[i][0];
      number -= map[i][1];
    } else {
      i++;
    }
  }

  return roman;
};

intToMiniRoman(19); // 'xix'
intToMiniRoman(152); // 'clii'
intToMiniRoman(426); // 'cdxxvi'

// Time Complexity: O(1)
// Space Complexity: O(1)

/*
  This function works by iterating over an array that maps roman numeral characters to their corresponding integer values. 
  It then subtracts the largest possible value from the input number and adds the corresponding roman numeral character to the result string.
  This process is repeated until the input number is 0. 
  Finally, it returns the result string.
  */

module.exports = {intToMiniRoman};

/*
  The code is written in JavaScript and uses the concept of roman numerals to convert an integer to its roman numeral equivalent.
  The function intToMiniRoman takes an integer as an argument and returns its roman numeral equivalent.
  It uses a map array that stores roman numeral characters as keys and their corresponding integer values as values.
  The function then iterates over the map array, subtracting the largest possible value from the input number and adding the corresponding roman numeral character to the result string.
  This process is repeated until the input number is 0.
  Finally, the function returns the result string.
  */

/*
  Test cases:

 