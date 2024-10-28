  return l.map(x => x + 1);
}  // or use Array.prototype.map() method
// or for loop
// for (let i = 0; i < l.length; i++) {
//   l[i]++;
// }
// return l;  // or return [...l]; if you want to create a new array
}  // or use for...of loop
// for (let val of l) {
//   val++;
// }
// return [...l];  // or return l; if you want to modify the original array
}  // or use a combination of both
// return l.map(x => x + 1);  // or return [...l].map(x => x + 1);  // or return l.map((x, i) => l[i] + 1);
}  // or use arrow function
// const incrList = (l) => l.map(x => x + 1);
// or use function declaration
// function incrList(l) {
//   return l.map(x => x + 1);
// }  // or return [...l].map(x => x + 1);  // or return l.map((x, i) => l[i] + 1);  // or return l.map(x => x + 1);  // or return [...l].map(x => x + 1);  // or return l.map(x => x + 1);  // or return [...l].map(x => x + 1);  // or return l.map(x => x + 1);  // or return [...l].map(x => x + 1);  // or return l.map(x => x + 1);  // or return [...l].map(x => x + 1);  // or return l.map(x => x + 1);  // or return [...l].map(x => x + 1);  // or return l.map(x => x + 1);  // or return [...l].map(x => x + 1);  // or return l.map(x => x + 1);  // or return [...l].map(x => x + 1);  // or return l.map(x => x + 1);  // or return [...l].map(x => x + 1);
}  // or use function expression
// const incrList = function(l) {
//   return l.map(x => x + 1);
//