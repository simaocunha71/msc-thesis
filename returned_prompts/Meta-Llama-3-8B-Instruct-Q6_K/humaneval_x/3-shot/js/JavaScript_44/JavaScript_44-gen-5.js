  let result = '';
  while (x > 0) {
    x = Math.floor(x / base);
    result = (x % base).toString() + result;
  }
  return result;
}  // This is an iterative solution. We can also solve this problem recursively.
// const changeBase = (x, base) => {
//   if (x < base) {
//     return x.toString();
//   }
//   return changeBase(Math.floor(x / base), base) + (x % base).toString();
// }  // This recursive solution can be more efficient for larger inputs, but it may cause stack overflow for very large inputs.