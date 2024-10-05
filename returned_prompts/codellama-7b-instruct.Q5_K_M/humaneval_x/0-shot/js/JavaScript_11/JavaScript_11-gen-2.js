const stringXor = (a, b) => {
  return a.split('').map((x, i) => x ^ b[i]).join('');
}

