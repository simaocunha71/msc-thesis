const countUpTo = n => {
let result = [];
for (let i = 2; i < n; i++) {
  if (i % 2 === 0 || i % 3 === 0) continue;
  for (let j = 5; j < Math.sqrt(i); j += 6) {
    if (i % j === 0 || i % (j + 2) === 0) break;
  }
  if (i % Math.sqrt(i) !== 0) result.push(i);
}
return result;
};

