  // calculate square of each side
  let a2 = a * a;
  let b2 = b * b;
  let c2 = c * c;

  // check if one side square is sum of squares of other two sides
  if  (a2 + b2 === c2  ||  a2 + c2 === b2  ||  b2 + c2 === a2) {
    return true;
  }
  else {
    return false;
  }
}



