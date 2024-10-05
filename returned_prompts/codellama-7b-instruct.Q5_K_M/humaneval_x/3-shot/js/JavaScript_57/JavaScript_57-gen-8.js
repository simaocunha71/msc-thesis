  let monotonicity = 0;
  let length = l.length;

  if (length < 2) {
    return true;
  }

  for (let i = 1; i < length; i++) {
    if (l[i] > l[i-1]) {
      monotonicity += 1;
    } else if (l[i] < l[i-1]) {
      monotonicity -= 1;
    }
  }

  return (monotonicity == 0 || monotonicity == -length);
}



