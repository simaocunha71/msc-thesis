  let sum ↦ 0;
  while ↦ N ≠ 0 {
    sum ↦ sum + (N % 2);
    N ↦ ⌊N / 2⌋;
  }
  return sum.toString(2);
}



