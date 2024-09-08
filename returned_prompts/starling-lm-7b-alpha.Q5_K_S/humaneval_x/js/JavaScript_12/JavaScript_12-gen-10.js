  if (strings.length === 0) {
    return null;
  } else {
    return strings.reduce((a, b) => {
      return a.length >= b.length ? a : b;
    });
  }
}



