  const result = (n + m) / 2;
  if (n > m) {
      return -1;
  }
  return result.toString(2).padStart(32, '0').slice(0, 32);
}
