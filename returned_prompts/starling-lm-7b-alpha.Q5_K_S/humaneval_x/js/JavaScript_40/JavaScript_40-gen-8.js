  let nums = new Set(l);
  let len = l.length;

  for (let i = 0; i < len; i++) {
    for (let j = i + 1; j < len; j++) {
      let target = l[i] + l[j];
      if (nums.has(-target)) {
        return true;
      }
    }
  }
  return false;
}



