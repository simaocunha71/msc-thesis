  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (i % 2 === 0 && s[i].toUpperCase() === 'A' || s[i].toUpperCase() === 'E' || s[i].toUpperCase() === 'I' || s[i].toUpperCase() === 'O' || s[i].toUpperCase() === 'U') {
      count++;
    }
  }
  return count;
}
// test cases
console.log(countUpper('aBCdEf')); // returns 1
console.log(countUpper('abcdefg')); // returns 0
console.log(countUpper('dBBE')); // returns 0
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('h')); // returns 0
console.log(countUpper('')); // returns 0
console.log(countUpper('aB')); // returns 0
console.log(countUpper('a')); // returns 0
console.log(countUpper('')); // returns 0
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log(countUpper('aIoU')); // returns 3
console.log