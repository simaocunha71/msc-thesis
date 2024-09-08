  if (s.length < 3) {
    return false;
  }

  const set = new Set();
  for (let i = 0; i < s.length - 2; i++) {
    const letters = s.slice(i, i + 3);
    if (set.has(letters)) {
      return false;
    }
    set.add(letters);
  }

  return true;
}



