const num = Math.pow(a, (1/3));
return (num % 1 === 0);
};


/*
  Write a function that takes a number and returns a string
  representing the same number, but in the form of Roman Numerals.
  Note: you may assume the input is always valid.
  Examples:
  toRoman(1) ==> "I"
  toRoman(2) ==> "II"
  toRoman(4) ==> "IV"
  toRoman(7) ==> "VII"
  toRoman(8) ==> "VIII"
  toRoman(14) ==> "XIV"
  toRoman(16) ==> "XVI"
  toRoman(24) ==> "XXIV"
  toRoman(25) ==> "XXV"
  toRoman(100) ==> "C"
  toRoman(200) ==> "CC"
  toRoman(300) ==> "CCC"
  toRoman(500) ==> "D"
  toRoman(600) ==> "DC"
  toRoman(800) ==> "DCCC"
  toRoman(1000) ==> "M"
  toRoman(1500) ==> "MC"
  toRoman(2000) ==> "MM"
  toRoman(2500) ==> "MMV"
  toRoman(3000) ==> "MMM"
  toRoman(3500) ==> "MMMD"
  toRoman(4000) ==> "MMMM"
 */

const toRoman = (a) => {
  const thousands = a / 1000;
  const hundreds = (a % 1000) / 100;
  const tens = (a % 100) / 10;
  const ones = a % 10;

  const thousandsMap = {
    M: thousands,
    CM: thousands - 900,
    D: thousands - 500,
    CD: thousands - 40