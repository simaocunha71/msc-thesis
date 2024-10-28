  let str = x.toString();
  if (shift >= str.length) {
    return str.split('').reverse().join('');
  } else {
    return str.slice(str.length - shift) + str.slice(0, str.length - shift);
  }
}



