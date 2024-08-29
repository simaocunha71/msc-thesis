  let len = string.length;
  if (len == 1) return false;
  for (let i = 2; i < len; i++) {
    if (len % i == 0) return false;
  }
  return true;
}



