  let str = String(x);
  let len = str.length;
  if (shift >= len) {
    return str.split('').reverse().join('');
  } else {
    return str.slice(len - shift) + str.slice(0, len - shift);
  }
}



