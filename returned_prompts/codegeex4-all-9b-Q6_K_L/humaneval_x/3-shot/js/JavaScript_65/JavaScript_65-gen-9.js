  let str = x.toString();
  if (shift > str.length) {
    return str.split('').reverse().join('');
  } else {
    return str.substring(shift) + str.substring(0, shift);
  }
}



