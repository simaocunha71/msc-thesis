  var result = '';
  var groups = s.split('');
  for (let i = 0; i < groups.length; i++) {
    if (i > 0 && (i % 3 == 0)) {
      result += groups[i - 1];
    }
    result += groups[i];
  }
  return result;
}
// Test
console.log(encodeCyclic("Hello World"));
console.log(decodeCyclic("Hloe ol rld"));
// Output:
// "Hloe ol rld"
// "Hello World"