  let result = 0;
  for (let i = 1; i <= n; i++) {
    result += (i * i - i + 1) % 3 == 0 ? 1 : 0;
  }
  return result;
}



