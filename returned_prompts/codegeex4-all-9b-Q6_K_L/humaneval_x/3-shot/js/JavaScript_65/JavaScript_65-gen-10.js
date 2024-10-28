  let xStr = x.toString();
  let shiftStr = shift.toString();

  if (shift > xStr.length) {
    return xStr.split('').reverse().join('');
  } else {
    return xStr.slice(shiftStr.length) + xStr.slice(0, shiftStr.length);
  }
}



