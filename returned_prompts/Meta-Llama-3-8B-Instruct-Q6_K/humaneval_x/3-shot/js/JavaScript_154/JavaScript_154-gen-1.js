  if (a.includes(b)) {
    return true;
  }
  for (let i = 0; i < a.length; i++) {
    if (a.slice(i, a.length).includes(b)) {
      return true;
    }
  }
  return false;
}