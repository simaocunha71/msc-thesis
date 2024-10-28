const sortEven = (l) => {
  const result = [];
  for (let i = 0; i < l.length; i++) {
    if (i % 2 === 0) {
      result.push(l[i]);
    } else {
      result.push(l[i].sort());
    }
  }
  return result;
};

const l = [1, 2, 3];
const expected = [1, 2, 3];
assert.deepStrictEqual(sortEven(l), expected);

const l = [5, 6, 3, 4];
const expected = [3, 6, 5, 4];
assert.deepStrictEqual(sortEven(l), expected);

const l = [1, 2, 3, 4, 5];
const expected = [1, 2, 3, 4, 5];
assert.deepStrictEqual(sortEven(l), expected);

const l = [5, 6, 3, 4, 1];
const expected = [1, 5, 3, 6, 4];
assert.deepStrictEqual(sortEven(l), expected);

const l = [1, 2, 3, 4, 5, 6];
const expected = [1, 2, 3, 4, 5, 6];
assert.deepStrictEqual(sortEven(l), expected);

const l = [5, 6, 3, 4, 1, 2];
const expected = [1, 5, 3, 6, 4, 2];
assert.deepStrictEqual(sortEven(l), expected);
