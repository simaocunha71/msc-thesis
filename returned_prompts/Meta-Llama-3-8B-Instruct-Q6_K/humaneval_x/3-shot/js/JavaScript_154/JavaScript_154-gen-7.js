  for (let i = 0; i < b.length; i++) {
    let rotate = b.substring(i) + b.substring(0, i);
    if (a.includes(rotate)) {
      return true;
    }
  }
  return false;
}
// OR
const cycpatternCheck = (a, b) => {
  for (let i = 0; i < b.length; i++) {
    let rotate = b.substring(i) + b.substring(0, i);
    if (a.includes(rotate) || a.includes(b)) {
      return true;
    }
  }
  return false;
}