  const aLength = a.length;
  const bLength = b.length;
  for (let i = 0; i < aLength; i++) {
    if (a.includes(b)) {
      return true;
    }
    a = a.slice(1) + a.slice(0, 1);
  }
  return false;
}

