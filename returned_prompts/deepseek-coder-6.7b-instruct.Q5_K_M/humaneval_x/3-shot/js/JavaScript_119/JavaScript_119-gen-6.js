  const s1 = lst[0] + lst[1];
  const s2 = lst[1] + lst[0];
  const isGood = s => {
    let count = 0;
    for (let c of s) {
      if (c == '(') {
        count++;
      } else {
        if (count == 0) {
          return false;
        }
        count--;
      }
    }
    return count == 0;
  }
  return isGood(s1) || isGood(s2) ? 'Yes' : 'No';
}



