  return strings.filter(str => str.startsWith(prefix));
} // Using ES6's filter() method and startsWith() method
// Alternatively, using a for loop:
// const filterByPrefix = (strings, prefix) => {
//   let result = [];
//   for (const str of strings) {
//     if (str.startsWith(prefix)) {
//       result.push(str);
//     }
//   }
//   return result;
// }