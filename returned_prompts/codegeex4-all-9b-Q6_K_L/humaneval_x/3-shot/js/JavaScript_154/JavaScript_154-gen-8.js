  let n = b.length;
  for (let i = 0; i < n; i++) {
    let rotate = b.slice(i) + b.slice(0, i);
    if (a.includes(rotate)) {
      return true;
    }
  }
  return false;
}