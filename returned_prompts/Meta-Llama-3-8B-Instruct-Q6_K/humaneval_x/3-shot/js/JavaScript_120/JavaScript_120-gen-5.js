  return arr.sort((a, b) => b - a).slice(0, k);
}
// You can also use the built-in function `Array.prototype.slice.call()` and `Array.prototype.sort()` to achieve the same result.
// const maximum = (arr, k) => Array.prototype.slice.call(arr.sort((a, b) => b - a), 0, k);