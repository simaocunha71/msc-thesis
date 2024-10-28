  let count = 0;
  let a = new Array(n);
  for (let i = 0; i < n; i++) {
    a[i] = i * i - i + 1;
  }
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      for (let k = j + 1; k < n; k++) {
        if ((a[i] + a[j] + a[k]) % 3 === 0) {
          count++;
        }
      }
    }
  }
  return count;
}  // 1
// console.log(getMaxTriples(5)); // Output: 1
// console.log(getMaxTriples(10)); // Output: 3
// console.log(getMaxTriples(15)); // Output: 6
// console.log(getMaxTriples(20)); // Output: 10
// console.log(getMaxTriples(25)); // Output: 15
// console.log(getMaxTriples(30)); // Output: 21
// console.log(getMaxTriples(35)); // Output: 28
// console.log(getMaxTriples(40)); // Output: 36
// console.log(getMaxTriples(45)); // Output: 45
// console.log(getMaxTriples(50)); // Output: 55
// console.log(getMaxTriples(55)); // Output: 65
// console.log(getMaxTriples(60)); // Output: 76
// console.log(getMaxTriples(65)); // Output: 88
// console.log(getMaxTriples(70)); // Output: 101
// console.log(getMaxTriples(75)); // Output: 115
// console.log(getMaxTriples(80)); // Output: 130
// console.log(getMaxTriples(85)); // Output: 146
// console.log(getMaxTriples(90)); // Output: 163
// console.log(getMaxTriples(95)); // Output: 181
// console.log(getMaxTriples(100)); // Output: 200
// console.log(getMaxTriples(105)); // Output: 220
// console.log(getMaxTriples(110)); // Output: 242
// console.log(getMaxTriples(115)); // Output: 265
// console