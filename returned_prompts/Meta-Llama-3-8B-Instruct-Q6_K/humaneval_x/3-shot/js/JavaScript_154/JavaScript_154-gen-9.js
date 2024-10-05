  for (let i = 0; i < b.length; i++) {
    let rotated_b = b.slice(i) + b.slice(0, i);
    if (a.includes(rotated_b)) {
      return true;
    }
  }
  return false;
}