  let result = "";
  for (let i = 0; i < a.length; i++) {
    result += (a[i] ^ b[i]) ? '1' : '0';
  }
  return result;
}



