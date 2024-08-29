  if (x > y) {
    return chooseNum(y, x);
  }

  if (y % 2 != 0) {
    return y - 1;
  } else {
    return y;
  }
}



