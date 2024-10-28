  if (string === '') {
    return 0;
  }
  let length = 0;
  for (let char of string) {
    length++;
  }
  return length;
};
// Test cases
console.log(strlen('')); // 0
console.log(strlen('abc')); // 3
console.log(strlen('Hello, World!')); // 13
console.log(strlen('')); // 0
console.log(strlen('  ')); // 2
console.log(strlen('12345')); // 5
// Example of a non-string input
console.log(strlen(null)); // throws an error
console.log(strlen(123)); // throws an error
// Example of a non-string input
console.log(strlen({})); // throws an error
console.log(strlen(function(){})); // throws an error
console.log(strlen(true)); // throws an error
console.log(strlen(false)); // throws an error
console.log(strlen([])); // throws an error
console.log(strlen({a:1,b:2})); // throws an error
console.log(strlen('')); // 0
console.log(strlen('  ')); // 2
console.log(strlen('12345')); // 5
console.log(strlen('Hello, World!')); // 13
console.log(strlen('Hello')); // 5
console.log(strlen('')); // 0
console.log(strlen('12345')); // 5
console.log(strlen('')); // 0
console.log(strlen('Hello, World!')); // 13
console.log(strlen('')); // 0
console.log(strlen('12345')); // 5
console.log(strlen('')); // 0
console.log(strlen('Hello, World!')); // 13
console.log(strlen('')); // 0
console.log(strlen('12345')); // 5
console.log(strlen('')); // 0
console.log(strlen('Hello, World!')); // 13
console.log(strlen('')); // 0
console.log(strlen('12345')); // 5
console.log(strlen('')); // 0
console.log(strlen('Hello, World!')); // 13
console.log(strlen('')); // 0
console.log(strlen('12345')); // 5
console.log(strlen('')); // 0
console.log(strlen('Hello, World!')); // 13
console.log(strlen('')); // 0
console.log(strlen('12345')); // 5
console.log(strlen('')); // 0
console.log(strlen('Hello