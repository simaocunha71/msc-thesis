/*
  let roman = '';
  const num = [
    [1000, 'm'],
    [900, 'cm'],
    [500, 'd'],
    [400, 'cd'],
    [100, 'c'],
    [90, 'xc'],
    [50, 'l'],
    [40, 'xl'],
    [10, 'x'],
    [9, 'ix'],
    [5, 'v'],
    [4, 'iv'],
    [1, 'i']
  ];
  for (let i = 0; i < num.length; i++) {
    while (number >= num[i][0]) {
      number -= num[i][0];
      roman += num[i][1];
    }
  }
  return roman;
*/
const intToMiniRoman = num => {
  const M = ["", "M", "MM", "MMM"];
  const C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
  const X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
  const I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
  return M[num / 1000 | 0] + C[(num / 100) % 10 | 0] + X[(num / 10) % 10 | 0] + I[num % 10 | 0];
};



B:
/*
  let roman = '';
  const num = [
    [1000, 'M'],
    [900, 'CM'],
    [500, 'D'],
    [400, 'CD'],
    [100, 'C'],
    [90, 'XC'],
    [50, 'L'],
    [40, 'XL'],
    [10