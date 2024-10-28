  for (let i = 0; i < a.length - b.length + 1; i++) {
    let substr = a.substring(i, i + b.length);
    if (b === substr) {
      return true;
    }
  }

  return false;
}



