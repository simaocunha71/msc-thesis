  const sorted = numbers.slice().sort((a, b) => a - b);
  const dist = Array.from({ length: sorted.length - 1 }, () => Infinity);
  let min = Infinity;
  let index = 0;

  for (let i = 0; i < sorted.length - 1; i++) {
    const diff = sorted[i + 1] - sorted[i];
    if (diff < min) {
      min = diff;
      index = i;
    }
    dist[i] = diff;
  }

  return [sorted[index], sorted[index + 1]];
};






/* From a supplied list of numbers (of length at least two) select and return two that are the closest to each
  other and return them in order (smaller number, larger number).
  >>> findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
  (2.0, 2.2)
  >>> findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
  (2.0, 2.0)
  */

function findClosestElements(numbers) {
  const sorted = [...numbers].sort((a, b) => a - b);
  const dist = Array(sorted.length - 1).fill(Infinity);
  let min = Infinity;
  let index = 0;

  for (let i = 0; i < sorted.length - 1; i++) {
    const diff = sorted[i + 1] - sorted[i];
    if (diff < min) {
      min = diff;
      index = i;
    }
    dist[i] = diff;
  }

  return [sorted[index], sorted[index + 1]];
}










































