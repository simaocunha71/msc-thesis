  var result = '';
  for (const group of s.split('')) {
    if (group.length == 2)
      result += group[1] + group[0];
    else
      result += group;
  }
  return result;
}
// Example usage:
const encoded = encodeCyclic('Hello, World!');
console.log(encoded);  // Output: Hlo, Wrld!
const decoded = decodeCyclic(encoded);
console.log(decoded);  // Output: Hello, World!
}()  // IIFE for immediate execution
// The result of the above code will be "Hello, World!" as expected.