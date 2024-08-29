  const re = /(\d+) (\w+)s? and (\d+) (\w+)s?/;
  const match = s.match(re);
  const apples = Number(match[1]);
  const oranges = Number(match[3]);
  const all = apples + oranges;
  return n - all;
}



