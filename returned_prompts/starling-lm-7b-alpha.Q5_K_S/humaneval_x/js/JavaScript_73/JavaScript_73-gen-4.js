  let mid = Math.floor(arr.length / 2);
  let left = arr.slice(0, mid);
  let right = arr.slice(arr.length - mid).reverse();
  let count = 0;

  for (let i = 0; i < mid; i++) {
    if (left[i] !== right[i]) {
      count += 1;
    }
  }

  return Math.min(count, arr.length - count);
}



