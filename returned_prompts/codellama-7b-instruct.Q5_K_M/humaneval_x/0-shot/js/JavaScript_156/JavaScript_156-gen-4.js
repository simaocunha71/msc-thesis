const romanNumeralMap = {
  1: 'i',
  5: 'v',
  10: 'x',
  50: 'l',
  100: 'c',
  500: 'd',
  1000: 'm',
};

const romanNumeralSubtractionMap = {
  4: 'iv',
  9: 'ix',
  40: 'xl',
  90: 'xc',
  400: 'cd',
  900: 'cm',
};

const toMiniRoman = (number) => {
  const numberString = number.toString();

  const firstDigit = numberString[0];
  const secondDigit = numberString[1];

  if (secondDigit !== undefined) {
    const subtractionKey = firstDigit + secondDigit;
    if (romanNumeralSubtractionMap[subtractionKey]) {
      return romanNumeralSubtractionMap[subtractionKey];
    }
  }

  const firstDigitValue = romanNumeralMap[firstDigit];
  return firstDigitValue;
};

const toRomanNumeral = (number) => {
  let romanNumeral = '';

  while (number > 0) {
    const miniRomanNumeral = toMiniRoman(number);
    romanNumeral += miniRomanNumeral;
    number -= miniRomanNumeral.length;
  }

  return romanNumeral;
};

const intToMiniRoman = (number) => {
  const romanNumeral = toRomanNumeral(number);
  return romanNumeral.toLowerCase();
};

const intToMiniRoman = (number) => {
  if (number > 5000 || number < 1) {
    throw new Error('Invalid input.');
  }

  const romanNumeral = toRomanNumeral(number);
  return romanNumeral.toLowerCase();
};

const intToMiniRoman = (number) =>