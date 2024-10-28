const prodSigns = (arr) => {
  if(!arr.length) return null;
  let product = 1;
  return arr.reduce((acc, cur) => {
    product *= cur > 0 ? 1 : cur < 0 ? -1 : 0;
    return acc + Math.abs(cur) * product;
  }, 0);
}

