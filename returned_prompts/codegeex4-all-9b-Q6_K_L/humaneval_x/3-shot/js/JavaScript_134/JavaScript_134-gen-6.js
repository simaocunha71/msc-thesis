  const regex = /^[a-z]$/i;
  const lastChar = txt.trim().slice(-1);
  return regex.test(lastChar);
}