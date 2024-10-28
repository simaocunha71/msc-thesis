const map = {
  "zero": 0,
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
};

const arr = numbers.split(" ").map(n => map[n]);

arr.sort((a, b) => a - b);

return arr.map(n => map[n]).join(" ");

};

sortNumbers('three one five') // 'one three five'






















*/
import assert from 'assert';
import { sortNumbers } from './solution';
describe('solution', function () {
  it('should be able to sort numbers from smallest to largest', function () {
    assert.strictEqual(sortNumbers('three one five'), 'one three five');
    assert.strictEqual(sortNumbers('nine one seven'), 'one seven nine');
    assert.strictEqual(sortNumbers('zero'), 'zero');
    assert.strictEqual(sortNumbers('four two'), 'two four');
    assert.strictEqual(sortNumbers('eight six seven'), 'six seven eight');
    assert.strictEqual(sortNumbers('nine eight seven'), 'seven eight nine');
    assert.strictEqual(sortNumbers('six six'), 'six six');
    assert.strictEqual(sortNumbers('one'), 'one');
    assert.strictEqual(sortNumbers('seven'), 'seven');
    assert.strictEqual(sortNumbers('nine'), 'nine');
  });
});
































































































