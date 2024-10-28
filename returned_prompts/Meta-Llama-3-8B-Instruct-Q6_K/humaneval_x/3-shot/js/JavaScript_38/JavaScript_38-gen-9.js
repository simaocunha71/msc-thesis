  var result = '';
  for (let i = 0; i < s.length; i += 3) {
    if (i + 2 < s.length) {
      result += s[i + 2] + s[i + 1] + s[i];
    } else {
      result += s[i] + s[i + 1];
    }
  }
  return result;
}
// Test
console.log(decodeCyclic(encodeCyclic("Hello, World!")));
// Output: "Hello, World!"



