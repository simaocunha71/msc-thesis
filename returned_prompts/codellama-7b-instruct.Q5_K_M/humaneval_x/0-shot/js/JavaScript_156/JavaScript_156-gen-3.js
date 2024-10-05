/*
  Roman numerals are a system of writing numbers using letters, with each letter
  representing a specific value. The values are as follows:
  I = 1
  V = 5
  X = 10
  L = 50
  C = 100
  D = 500
  M = 1000

  There are also subtractive values. For example, 4 is X - I, or 9 is IX.

  To write numbers using Roman numerals, we can start with the biggest values
  and work our way down. We can use the subtractive values to build larger
  numbers. For example, to write 19, we can use XIX, which is built from the
  values of X and I.

  To convert a number to its Roman numeral equivalent, we can start by writing
  the biggest values that are less than or equal to the number. We can then
  subtract these values from the number, and continue until the number is 0.
  */

  const romanNumerals = ['M', 'D', 'C', 'L', 'X', 'V', 'I'];
  const romanValues = [1000, 500, 100, 50, 10, 5, 1];

  let romanNumeral = '';

  for (let i = 0; i < romanValues.length; i++) {
    while (number >= romanValues[i]) {
      number -= romanValues[i];
      romanNumeral += romanNumerals[i];
    }
  }

  return romanNumeral;
};
