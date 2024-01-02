/*Return median of elements in the list l.
  >>> median([3, 1, 2, 4, 5])
  3
  >>> median([-10, 4, 6, 1000, 10, 20])
  8.0
  */
const median = (l) => {
  if (!Array.isArray(l)) return NaN;
  const n = l.length;
  // O(n^2)
  const sorted = [...new Set([...l].sort((a, b) => a - b)));
  // O(1)
  return (sorted[Math.floor(n / 2)] || 0);
}