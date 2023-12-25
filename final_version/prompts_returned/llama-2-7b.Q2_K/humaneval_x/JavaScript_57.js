/*Return true is list elements are monotonically increasing or decreasing.
  >>> monotonic([1, 2, 4, 20])
  true
  >>> monotonic([1, 20, 4, 10])
  false
  >>> monotonic([4, 1, 0, -10])
  true
  */
const monotonic = (l) => {
  let a = l[0];
  for (let i in l) {
    if (!(a >= l[i])) return false;
  }
  return true;
}
