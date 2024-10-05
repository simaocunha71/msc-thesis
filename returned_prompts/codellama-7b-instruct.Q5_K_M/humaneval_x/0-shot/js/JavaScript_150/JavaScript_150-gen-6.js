
// I'd prefer to use a ternary operator here, but I don't think it's possible
const xOrY = (n, x, y) => {
  if (n % 2 !== 0 && n % 3 !== 0) {
    return x;
  }
  return y;
};

// I'd prefer to use a ternary operator here, but I don't think it's possible
// function xOrY(n, x, y) {
//   if (n % 2 !== 0 && n % 3 !== 0) {
//     return x;
//   }
//   return y;
// }

// function xOrY(n, x, y) {
//   return n % 2 !== 0 && n % 3 !== 0 ? x : y;
// }

// const xOrY = (n, x, y) => {
//   if (n % 2 === 0 || n % 3 === 0) {
//     return y;
//   }
//   return x;
// };

// const xOrY = (n, x, y) => {
//   if (n % 2 !== 0 && n % 3 !== 0) {
//     return x;
//   }
//   return y;
// };

// const xOrY = (n, x, y) => {
//   if (n % 2 !== 0 && n % 3 !== 0) {
//     return x;
//   }
//   return y;
// };

// function xOrY(n, x, y) {
//   if (n % 2 !== 0 && n % 3 !== 0) {
//     return x;
//   }
//   return y;
// }
