  const [a, o] = s.split(' and ').map(x => parseInt(x.split(' ')[0]));
  return n - a - o;
}



