  for (let i = 0; i < b.length; i++) {
    let rot = b.substring(i) + b.substring(0, i);
    if (a.includes(rot)) {
      return true;
    }
  }
  return false;
}