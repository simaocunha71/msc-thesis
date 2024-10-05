  let arr = [];
  while (n > 0) {
    if (n % 2 === 0) {
      arr.push(n);
      n--;
    } else {
      arr.push(n);
      n += 2;
    }
  }
  return arr;
};

makeAPile(3); // [3, 5, 7]

*/

makeAPile(4); // [4, 6, 8]

makeAPile(7); // [7, 9, 11]

makeAPile(10); // [10, 12, 14]

makeAPile(12); // [12, 14, 16]

makeAPile(14); // [14, 16, 18]

makeAPile(15); // [15, 17, 19]

makeAPile(16); // [16, 18, 20]

makeAPile(17); // [17, 19, 21]

makeAPile(18); // [18, 20, 22]

makeAPile(19); // [19, 21, 23]

makeAPile(20); // [20, 22, 24]

makeAPile(21); // [21, 23, 25]

makeAPile(22); // [22, 24, 26]

makeAPile(23); // [23, 25, 27]

makeAPile(24); // [24, 26, 28]

makeAPile(25); // [25, 27, 29]

makeAPile(26); // [26, 28, 30]

makeAPile(27); // [27, 29, 31]

makeAPile(28); // [28, 30, 32]

makeAPile(2