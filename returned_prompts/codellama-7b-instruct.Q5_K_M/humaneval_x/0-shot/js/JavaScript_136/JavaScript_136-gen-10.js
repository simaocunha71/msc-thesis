const largestSmallestIntegers = (list) => {

const largest = (a, b) => a > b ? a : b;
const smallest = (a, b) => a < b ? a : b;

const largestNegative = list.reduce((acc, cur) => {
  if (cur < 0 && (acc === null || acc < cur)) return cur;
  return acc;
}, null);

const smallestPositive = list.reduce((acc, cur) => {
  if (cur > 0 && (acc === null || acc > cur)) return cur;
  return acc;
}, null);

return [smallestPositive === null ? null : smallest(smallestPositive),
        largestNegative === null ? null : largest(largestNegative)];
}
