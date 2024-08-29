  let count = 0;
  for (let i = 0; i < lst[0].length; i++) {
    if (lst[0][i] === '(') {
      count += 1;
    } else {
      count -= 1;
    }
    if (count < 0) {
      return 'No';
    }
  }
  count = 0;
  for (let i = 0; i < lst[1].length; i++) {
    if (lst[1][i] === ')') {
      count += 1;
    } else {
      count -= 1;
    }
    if (count < 0) {
      return 'No';
    }
  }
  if (count !== 0) {
    return 'No';
  }
  return 'Yes';
}



