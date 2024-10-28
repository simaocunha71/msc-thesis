/*
  Write a function that takes in a string and returns the string with an "!" added to the end. However, if the string already ends with "!", then the output string should have "!!!" added to the end instead.

  Examples:
  end_me_up("Hey") ➞ "Hey!"
  end_me_up("Chill") ➞ "Chill!"
  end_me_up("Okay") ➞ "Okay!"
  end_me_up("Okay!") ➞ "Okay!!!"
  end_me_up("Hey!") ➞ "Hey!!!"
*/

//     function end_me_up(str) {
//       if (str.endsWith('!') === true) {
//         return str + '!!!'
//       }
//       return str + '!'
//     }
// console.log(end_me_up("Hey"));

//     function end_me_up(str) {
//       if (str.endsWith('!') === true) {
//         return str + '!!!'
//       }
//       return str + '!'
//     }
// console.log(end_me_up("Hey"));

B:
/*
  Write a function that takes in a non-negative integer and returns the number of bits that are equal to 1 in the binary representation of that integer.

  Examples:
  find_bits(0) ➞ 0
  find_bits(1) ➞ 1
  find_bits(2) ➞ 1
  find_bits(3) ➞ 2
  find_bits(4) ➞ 1
  find_bits(5) ➞ 2
  find_bits(6) ➞ 2
  find_bits(7) ➞ 3
  find_bits(8) ➞ 1
  find_bits(9) ➞ 2
  find_bits(10) ➞ 2
  find_bits(11) ➞ 3