  const diff = (a, b) => a - b;
  const is_increasing = l.map((e, i, l) => i == 0 ? 0 : diff(l[i], l[i-1])).every(e => e >= 0);
  const is_decreasing = l.map((e, i, l) => i == 0 ? 0 : diff(l[i], l[i-1])).every(e => e <= 0);
  return is_increasing || is_decreasing;
}



