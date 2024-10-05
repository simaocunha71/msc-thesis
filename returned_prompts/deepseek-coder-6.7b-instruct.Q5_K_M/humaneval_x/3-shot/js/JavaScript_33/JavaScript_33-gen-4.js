  let arr = l.map((num, i) => i % 3 === 0 ? [num].sort((a, b) => a - b) : num).map((num) => Array.isArray(num) ? num[0] : num);
  return arr;
}



