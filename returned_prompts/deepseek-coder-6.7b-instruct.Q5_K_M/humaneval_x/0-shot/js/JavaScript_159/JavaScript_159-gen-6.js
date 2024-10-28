  const total = number;
  const eaten = Math.min(need, remaining);
  const left = remaining - eaten;
  
  return [total + eaten, left];
}
*/

const eat = (number, need, remaining) => {
  const total = number;
  const eaten = Math.min(need, remaining);
  const left = remaining - eaten;

  return [total + eaten, left];
};

console.log(eat(5, 6, 10)); // -> [11, 4]
console.log(eat(4, 8, 9)); // -> [12, 1]
console.log(eat(1, 10, 10)); // -> [11, 0]
console.log(eat(2, 11, 5)); // -> [7, 0]

// Test Cases
console.assert(JSON.stringify(eat(5, 6, 10)) === JSON.stringify([11, 4]));
console.assert(JSON.stringify(eat(4, 8, 9)) === JSON.stringify([12, 1]));
console.assert(JSON.stringify(eat(1, 10, 10)) === JSON.stringify([11, 0]));
console.assert(JSON.stringify(eat(2, 11, 5)) === JSON.stringify([7, 0]));
console.assert(JSON.stringify(eat(0, 0, 0)) === JSON.stringify([0, 0]));
console.assert(JSON.stringify(eat(500, 500, 500)) === JSON.stringify([1000, 0]));
console.assert(JSON.stringify(eat(250, 250, 250)) === JSON.stringify([500, 0]));
console.assert(JSON.stringify(eat(0, 1000, 1000)) === JSON.stringify([1000, 0]));
