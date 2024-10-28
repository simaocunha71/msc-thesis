  for (let i = 0; i < a.length; i++) {
    if (a.substring(i) + a.substring(0, i) === b) {
      return true;
    }
  }
  return false;
}