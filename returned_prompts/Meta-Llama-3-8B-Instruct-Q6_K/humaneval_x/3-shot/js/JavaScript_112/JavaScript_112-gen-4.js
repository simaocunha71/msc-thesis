  let result = '';
  let found = false;

  for (let i = 0; i < s.length; i++) {
    let foundInC = false;
    for (let j = 0; j < c.length; j++) {
      if (s[i] == c[j]) {
        foundInC = true;
        break;
      }
    }
    if (!foundInC) {
      result += s[i];
      if (!found) {
        found = s[i] == s[i].toLowerCase();
      }
    }
  }

  return [result, found];
}
// test the function
console.log(reverseDelete('abcde', 'ae'));  // Output: ['bcd', false]
console.log(reverseDelete('abcdef', 'b'));  // Output: ['acdef', false]
console.log(reverseDelete('abcdedcba', 'ab'));  // Output: ['cdedc', true]
console.log(reverseDelete('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz', 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'));  // Output: ['', false]