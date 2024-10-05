  if (a < 0) {
    a = -a;
  }

  let i = 0;
  let j = a;

  while (i <= j) {
    let mid = Math.floor((i + j) / 2);
    let cube = mid * mid * mid;

    if (cube == a) {
      return true;
    } else if (cube < a) {
      i = mid + 1;
    } else {
      j = mid - 1;
    }
  }

  return false;
}



