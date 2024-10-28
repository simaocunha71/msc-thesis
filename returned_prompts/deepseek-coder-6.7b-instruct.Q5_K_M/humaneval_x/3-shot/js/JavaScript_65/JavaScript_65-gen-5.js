  let strX = String(x);
  if (shift >= strX.length) {
    return strX.split('').reverse().join('');
  } else {
    return strX.slice(-shift) + strX.slice(0, -shift);
  }
}



