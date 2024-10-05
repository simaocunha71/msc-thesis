  const s = l.slice(1).map((e, i) => e - l[i]);
  return s.every((e, i) => e >= 0 === s[i - 1] >= 0);
};

