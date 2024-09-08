  let b_rot = b + b;
  let b_length = b.length;
  for (let i = 0; i < a.length; i++) {
    if (a.substring(i, i + b_length) === b ||
      a.substring(i, i + b_length) === b_rot.substring(b_length, 2 * b_length)) {
      return true;
    }
  }
  return false;
}



