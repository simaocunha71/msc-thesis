  let min = Number.MAX_SAFE_INTEGER;
  let cur = 0;
  for (const n of nums) {
    cur += n;
    if (cur < min) {
      min = cur;
    }
    if (cur < 0) {
      cur = 0;
    }
  }
  return min;
}



