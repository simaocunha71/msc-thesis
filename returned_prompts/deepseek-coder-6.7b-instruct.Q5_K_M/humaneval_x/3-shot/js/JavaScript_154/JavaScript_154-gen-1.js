  if (a.includes(b)) {
    return true;
  }

  for (let i = 0; i < b.length; i++) {
    let rot = b.slice(i) + b.slice(0, i);
    if (a.includes(rot)) {
      return true;
    }
  }

  return false;
}



