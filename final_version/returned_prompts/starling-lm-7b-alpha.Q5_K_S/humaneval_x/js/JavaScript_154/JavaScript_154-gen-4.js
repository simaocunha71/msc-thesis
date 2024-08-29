  let rotatedString = b + b;
  let index = rotatedString.indexOf(a);
  if (index > -1) {
    return true;
  }
  return rotatedString.indexOf(rotatedString.slice(1, rotatedString.length) + rotatedString.slice(0, 1)) > -1;
}



