  let openCount = 0;
  for (let i = 0; i < lst[0].length; i++) {
    if (lst[0][i] == '(') {
      openCount++;
    } else {
      openCount--;
      if (openCount < 0) {
        return 'No';
      }
    }
  }
  if (openCount != 0) {
    return 'No';
  }

  openCount = 0;
  for (let i = 0; i < lst[1].length; i++) {
    if (lst[1][i] == ')') {
      openCount++;
    } else {
      openCount--;
      if (openCount < 0) {
        return 'No';
      }
    }
  }
  if (openCount != 0) {
    return 'No';
  }

  return 'Yes';
}



