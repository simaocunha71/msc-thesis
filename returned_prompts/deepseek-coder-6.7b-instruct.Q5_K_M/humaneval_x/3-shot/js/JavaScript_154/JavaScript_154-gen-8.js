  for (let i = 0; i < b.length; i++) {
    if (a.includes(b)) return true;
    b = b.slice(1) + b[0];
  }
  return false;
}



