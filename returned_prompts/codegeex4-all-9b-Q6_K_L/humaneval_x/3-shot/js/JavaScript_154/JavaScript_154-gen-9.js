  for (let i = 0; i < b.length; i++) {
    let rotatedString = b.slice(i) + b.slice(0, i);
    if (a.includes(rotatedString)) {
      return true;
    }
  }
  return false;
}