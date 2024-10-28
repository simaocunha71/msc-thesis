const stringXor = (a, b) => {
  return a.split('').map((char, index) => +(char ^ b[index])).join('');
}

