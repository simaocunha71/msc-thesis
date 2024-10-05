  const range = [];
  let min = Math.min(a, b);
  let max = Math.max(a, b);

  for (let i = min + 1; i < max; i++) {
    if (i % 2 === 0) {
      range.push(i);
    }
  }

  return range;
};

const test = require('ava');
test('generateIntegers', t => {
  t.is(generateIntegers(2, 8), [2, 4, 6, 8]);
  t.is(generateIntegers(8, 2), [2, 4, 6, 8]);
  t.is(generateIntegers(10, 14), []);
});
