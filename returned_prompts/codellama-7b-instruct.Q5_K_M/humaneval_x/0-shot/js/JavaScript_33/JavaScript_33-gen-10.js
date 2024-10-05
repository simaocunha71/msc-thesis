const sortFourth = (l) => {
  const arr = l.filter((e, i) => i % 4 !== 0).sort((a, b) => a - b);
  return l.map((e, i) => (i % 4 === 0 ? e : arr[i]));
};
