  let val = [
    1000, 900, 500, 400,
    100, 90, 50, 40,
    10, 9, 5, 4,
    1
  ];
  let syb = [
    "M", "CM", "D", "CD",
    "C", "XC", "L", "XL",
    "X", "IX", "V", "IV",
    "I"
  ];
  let roman = "";
  let i = 0;
  while (number > 0) {
    if (number >= val[i]) {
      number -= val[i];
      roman += syb[i];
    } else {
      i++;
    }
  }
  return roman.toLowerCase();
}