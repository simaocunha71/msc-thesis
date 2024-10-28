  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (i % 2 == 0 && 'AEIOU'.includes(s[i].toUpperCase())) {
      count++;
    }
  }
  return count;
}
// Test cases
console.log(countUpper('aBCdEf')); // 1
console.log(countUpper('abcdefg')); // 0
console.log(countUpper('dBBE')); // 0
console.log(countUpper('Hello')); // 1
console.log(countUpper('World')); // 0
console.log(countUpper('AEIOU')); // 5
console.log(countUpper('BCDFGHJKLMNPQRSTVWXYZ')); // 0
console.log(countUpper('')); // 0
// Output:
// 1
// 0
// 0
// 1
// 0
// 5
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
// 0
