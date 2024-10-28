  return l1.filter((x) => l2.includes(x))
  .sort()
  .filter((x, i, a) => a.indexOf(x) === i);
}



