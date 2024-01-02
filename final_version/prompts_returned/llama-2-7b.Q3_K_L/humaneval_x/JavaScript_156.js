/*
  Given a positive integer, obtain its roman numeral equivalent as a string,
  and return it in lowercase.
  Restrictions: 1 <= num <= 1000

  Examples:
  >>> intToMiniRoman(19) == 'xix'
  >>> intToMiniRoman(152) == 'clii'
  >>> intToMiniRoman(426) == 'cdxxvi'
  */
const intToMiniRoman = (number) => {
  const [str, ...arr] = number.toString().split('').reverse()
  return str + arr.reduce((acc, val) => ` ${acc}`, '')
}
