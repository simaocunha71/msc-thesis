  let arr = [...l];
  let sortedThird = arr.filter((_, i) => (i+1) % 3 === 0).sort((a, b) => a - b);
  return arr.map((v, i) => (i+1) % 3 === 0 ? sortedThird.shift() : v);
}



