  const str = String(x);
  if (shift >= str.length) {
    return str.split('').reverse().join('');
  }
  return str.slice(-shift) + str.slice(0, -shift);
}



