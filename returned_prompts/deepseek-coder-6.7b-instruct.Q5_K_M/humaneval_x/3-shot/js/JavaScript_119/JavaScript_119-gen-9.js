  let s1 = lst[0];
  let s2 = lst[1];
  let count = 0;

  for (let i = 0; i < s1.length; i++) {
    if (s1[i] == '(') {
      count += 1;
    } else {
      if (count == 0) {
        return 'No';
      }
      count -= 1;
    }
  }

  for (let i = 0; i < s2.length; i++) {
    if (s2[i] == '(') {
      count += 1;
    } else {
      if (count == 0) {
        return 'No';
      }
      count -= 1;
    }
  }

  return count == 0 ? 'Yes' : 'No';
}



