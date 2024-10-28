  let sorted = l.filter((_, i) => i % 2 === 0).sort((a, b) => a - b);
  return l.map((v, i) => (i % 2 === 0) ? sorted.shift() : v);
}

console.log(sortEven([5, 6, 3, 4]))


*/

