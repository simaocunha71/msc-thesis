  if (s.length < 3) {
    return false;
  }

  for (let i = 0; i < s.length - 2; i++) {
    let sub = s.slice(i, i + 3);
    if (sub.includes(sub[0], 1)) {
      return false;
    }
  }

  return true;
}



