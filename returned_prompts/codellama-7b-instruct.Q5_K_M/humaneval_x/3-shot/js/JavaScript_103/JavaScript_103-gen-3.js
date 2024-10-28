  if (n > m) {
    return -1;
  }

  const sum = n + m;
  const avg = sum / 2;
  const rounded = Math.round(avg);
  const binary = rounded.toString(2);
  return binary;
}



