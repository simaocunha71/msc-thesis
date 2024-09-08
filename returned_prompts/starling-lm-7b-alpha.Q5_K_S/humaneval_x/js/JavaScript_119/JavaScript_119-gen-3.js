  let left = 0;
  let right = 0;
  let lst_len = lst[0].length;
  for (let i = 0; i < lst_len; i++) {
    if (lst[0][i] == '(') {
      left += 1;
    } else {
      left -= 1;
    }
    if (lst[1][i] == ')') {
      right -= 1;
    } else {
      right += 1;
    }
    if (left < 0 || right < 0) {
      return "No";
    }
  }
  if (left == 0 && right == 0) {
    return "Yes";
  } else {
    return "No";
  }
}



