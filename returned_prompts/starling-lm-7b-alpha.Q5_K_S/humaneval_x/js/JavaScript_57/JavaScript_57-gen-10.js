  let isAscending = true;
  let isDescending = true;

  for (let i = 1; i < l.length; i++) {
    if (l[i] < l[i - 1]) {
      isAscending = false;
    }
    if (l[i] > l[i - 1]) {
      isDescending = false;
    }
  }

  return isAscending || isDescending;
}



