const splitWords = (txt) => {
  const re = /\s+/;
  if (re.test(txt)) {
    return txt.split(re);
  }
  if (re.test(txt)) {
    return txt.split(re);
  }
  return (txt.match(/[a-z]/g).length);
};
