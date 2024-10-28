  if (s.length < 3) {
    return false;
  }
  for (let i = 0; i < s.length - 2; i++) {
    let trio = s.substring(i, i + 3);
    if (trio.length !== 3 || trio.indexOf(trio[0]) !== -1 || trio.indexOf(trio[1]) !== -1 || trio.indexOf(trio[2]) !== -1) {
      return false;
    }
  }
  return true;
}