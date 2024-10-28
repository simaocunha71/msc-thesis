  let flag = 0;

  for (let i = 0; i < lst.length - 1; i++) {
    if (lst[i] > lst[i + 1]) {
      flag = 1;
    }
  }

  for (let j = 0; j < lst.length - 1; j++) {
    if (lst[j] == lst[j + 1]) {
      flag = 0;
    }
  }

  if (flag == 0) {
    return true;
  } else {
    return false;
  }
}



