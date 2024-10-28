  let s1 = lst[0];
  let s2 = lst[1];
  let balance = 0;

  for  (let i = 0; i < s1.length; i++) {
    if  (s1[i] == '(') {
      balance++;
    } else {
      balance--;
    }
    if  (balance < 0) {
      return 'No';
    }
  }

  if  (balance == 0) {
    return 'Yes';
  }

  balance = 0;

  for  (let i = 0; i < s2.length; i++) {
    if  (s2[i] == '(') {
      balance++;
    } else {
      balance--;
    }
    if  (balance < 0) {
      return 'No';
    }
  }

  return (balance == 0) ? 'Yes' : 'No';
}



