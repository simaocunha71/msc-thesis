const unique = (l) => {
  return l.filter((v, i) => {
    return l.indexOf(v) === i;
  });
}
