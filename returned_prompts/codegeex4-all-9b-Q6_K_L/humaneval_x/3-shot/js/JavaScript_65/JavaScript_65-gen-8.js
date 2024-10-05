  let s = x.toString();
  let n = s.length;

  if (shift > n) {
    return s.split('').reverse().join('');
  } else {
    return s.slice(n - shift) + s.slice(0, n - shift);
  }
}