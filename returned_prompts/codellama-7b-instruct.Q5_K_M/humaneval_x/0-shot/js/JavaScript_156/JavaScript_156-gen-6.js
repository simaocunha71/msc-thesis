

const intToRoman = (number) => {
  const roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
  const values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
  let romanString = '';

  for (let i = 0; i < values.length; i++) {
    let count = Math.floor(number / values[i]);
    number -= count * values[i];
    romanString += roman[i].repeat(count);
  }
  return romanString;
};

const intToMiniRoman = (number) => {
  const roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M'];
  const values = [1, 5, 10, 50, 100, 500, 1000];

  for (let i = 0; i < values.length; i++) {
    let count = 0;
    while (number >= values[i]) {
      count++;
      number -= values[i];
    }
    if (count > 0) {
      return roman[i].repeat(count);
    }
  }
};
