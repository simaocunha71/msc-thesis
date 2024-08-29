  if (n > m) return -1;

  let avg = Math.round((n + m) / 2);
  let binary = (avg).toString(2);

  return `0b${binary}`;
}



