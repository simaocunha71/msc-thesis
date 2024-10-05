const findClosestElements = (numbers) => {

const closestNumbers = numbers.reduce((closest, current) => {
  const [a, b] = closest;
  const diffA = Math.abs(a - current);
  const diffB = Math.abs(b - current);
  if (diffA < diffB) return [a, current];
  if (diffB < diffA) return [current, b];
  return closest;
}, [null, null]);

return [closestNumbers[0], closestNumbers[1]];
};