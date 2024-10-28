  var count = 0;

  for (let c of lst[0]) {
    if (c == '(') {
      count += 1;
    } else {
      count -= 1;
    }
  }

  for (let c of lst[1]) {
    if (c == '(') {
      count += 1;
    } else {
      count -= 1;
    }
  }

  if (count == 0) {
    return 'Yes';
  } else {
    return 'No';
  }
}



