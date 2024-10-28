  var left = 0;
  var right = 0;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] == '(') {
      left += 1;
    } else {
      right += 1;
    }
  }
  if (left == right) {
    return 'Yes';
  } else {
    return 'No';
  }
}



