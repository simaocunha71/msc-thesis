  if (s.length < 3) return false;
  for (let i = 0; i <= s.length - 3; i++) {
    let temp = s.slice(i, i + 3);
    if (temp.length !== 3 || temp.includes(temp[0], 1)) return false;
  }
  return true;
}