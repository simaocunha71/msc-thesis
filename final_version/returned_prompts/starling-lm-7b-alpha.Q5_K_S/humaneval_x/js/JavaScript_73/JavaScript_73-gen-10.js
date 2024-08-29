  let n = arr.length;
  let mid = Math.floor(n / 2);

  let left = arr.slice(0, mid);
  let right = arr.slice(mid).reverse();

  let count = 0;

  for (let i = 0; i < mid; i++) {
    if (left[i] != right[i]) {
      count += 1;
    }
  }

  return count;
}



