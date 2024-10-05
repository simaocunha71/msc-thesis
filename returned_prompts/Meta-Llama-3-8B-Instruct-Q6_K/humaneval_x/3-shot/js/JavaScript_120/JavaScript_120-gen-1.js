  return arr.sort((a, b) => b - a).slice(0, k);
}
// or
const maximum = (arr, k) => {
  return arr.sort((a, b) => b - a).slice(0, k).reverse();
} // Note: This is not necessary, but can be used to maintain the original order of equal elements.