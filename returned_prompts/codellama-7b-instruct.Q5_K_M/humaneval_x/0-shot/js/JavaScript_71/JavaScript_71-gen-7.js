/*
  Given the lengths of the three sides of a triangle. Return the area of
  the triangle rounded to 2 decimal points if the three sides form a valid triangle.
  Otherwise return -1
  Three sides make a valid triangle when the sum of any two sides is greater
  than the third side.
  Example:
  triangleArea(3, 4, 5) == 6.00
  triangleArea(1, 2, 10) == -1
  */
const triangleArea = (a, b, c) => {
  const isValid = a + b > c;
  const area = isValid ? (a * b * Math.sqrt(1 - Math.pow(Math.sin(Math.atan2(b - a, a + b)), 2))) / 2 : -1;
  return area.toFixed(2);
};

/*
  Given a string, return a new string where every char is the char after the
  given number steps right in the alphabet.
  Note:
  - assume the alphabet only has 26 letters
  - use the manhattan distance (https://en.wikipedia.org/wiki/Taxicab_geometry)
  - if the letter is at the end of the alphabet, wrap around to the beginning
  - if the letter is at the beginning of the alphabet, wrap around to the end
  - if the input string is empty, return an empty string
  Examples:
  rightOf("a", 2) === "c"
  rightOf("z", 22) === "b"
  rightOf("abc", 1) === "bcd"
  rightOf("xyz", 2) === "abc"
  rightOf("", 52) === ""
  */
const rightOf = (str, steps) => {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  const arr = str.split('');
  const newArr = arr.map(char => {
    const idx = alphabet.indexOf(char);
    const newIdx = idx + steps;
    return alphabet[newIdx % 26];
  });
  return newArr.join('');
};

/*
  Given