/* From a supplied list of numbers (of length at least two) select and return two that are the closest to each
  other and return them in order (smaller number, larger number).
  >>> findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
  (2.0, 2.2)
  >>> findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
  (2.0, 2.0)
  */
const findClosestElements = (numbers) => {
  const diffs = numbers.map((num, idx, arr) => {
    const next = arr[idx + 1]
    return next ? Math.abs(num - next) : Infinity
  })
  const idx = diffs.indexOf(Math.min(...diffs))
  return [numbers[idx], numbers[idx + 1]]
}
