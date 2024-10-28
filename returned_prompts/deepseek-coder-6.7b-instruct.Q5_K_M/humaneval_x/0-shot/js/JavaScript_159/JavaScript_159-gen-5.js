  let total = number
  let left = remaining
  
  if (need < remaining) {
    total += need
    left -= need
  } else {
    total += remaining
    left = 0
  }

  return [total, left]
}
*/

const eat = (number, need, remaining) => {
  let total = number;
  let left = remaining;

  if (need < remaining) {
    total += need;
    left -= need;
  } else {
    total += remaining;
    left = 0;
  }

  return [total, left];
};

console.log(eat(5, 6, 10)); // -> [11, 4]
console.log(eat(4, 8, 9)); // -> [12, 1]
console.log(eat(1, 10, 10)); // -> [11, 0]
console.log(eat(2, 11, 5)); // -> [7, 0]
