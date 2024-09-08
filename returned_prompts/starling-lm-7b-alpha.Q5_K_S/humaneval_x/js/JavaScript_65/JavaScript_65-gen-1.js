  const digits = String(x).split('');
  const len = digits.length;
  const end = (shift % len);
  const start = (len - end) % len;
  const result = digits.slice(start, end);
  const other = digits.slice(0, start).concat(digits.slice(end, len));
  return result.concat(other).join('');
}



