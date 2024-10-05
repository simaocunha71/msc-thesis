  const roman_numerals = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i'];
  const roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
  let roman = '';

  for (let i = 0; i < roman_values.length; i++) {
    while (number >= roman_values[i]) {
      number -= roman_values[i];
      roman += roman_numerals[i];
    }
  }

  return roman.toLowerCase();
}
// Example usage:
console.log(intToMiniRoman(19)); // Outputs: "xix"
console.log(intToMiniRoman(152)); // Outputs: "clii"
console.log(intToMiniRoman(426)); // Outputs: "cdxxvi"