  if (n > m) {
    return -1;
  }

  const sum = (m - n + 1) * (n + m) / 2;
  const rounded = Math.round(sum);
  const binary = rounded.toString(2);

  return `0b${binary}`;
}

