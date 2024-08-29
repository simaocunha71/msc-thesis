  let count = 0;
  for (let i = 0; i < hex_str.length; i++) {
    const num = hexKey(hex_str[i]);
    if (isPrime(num)) {
      count += 1;
    }
  }
  return count;
};



