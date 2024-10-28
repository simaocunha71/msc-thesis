  return strings.filter(str => str.startsWith(prefix));
} // use of built-in function startsWith() from ES6
// alternative implementation without ES6
// return strings.filter(function(str) {
//   return str.substring(0, prefix.length) === prefix;
// }); 



