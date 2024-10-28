  return l.map((value, index) => {
    if (index % 2 === 0) {
      return l.slice(0, index).slice(-1)[0];
    } else {
      return value;
    }
  });
}